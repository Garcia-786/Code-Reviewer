import reflex as rx
import time
from typing import List, Dict, Any
from .core.analyzer import analyze_code_basic
from .core.ai_helper import analyze_code_with_ai, chat_with_aibot
from .core.history_db import get_history, add_to_history, delete_history_item

class AnalysisResult(rx.Base):
    syntax_errors: List[str]
    style_errors: List[str]
    ai_issues: List[str]
    ai_optimizations: List[str]
    time_complexity: str
    space_complexity: str
    optimized_code: str

class HistoryItem(rx.Base):
    id: str
    code: str
    timestamp: float
    analysis: AnalysisResult

class ChatMessage(rx.Base):
    role: str
    content: str

class AppState(rx.State):
    """The app state."""
    pass

class AnalyzerState(AppState):
    input_code: str = ""
    is_loading: bool = False
    
    # Analysis results
    syntax_errors: List[str] = []
    style_errors: List[str] = []
    is_valid: bool = True
    
    # AI Results
    ai_issues: List[str] = []
    ai_optimizations: List[str] = []
    time_complexity: str = ""
    space_complexity: str = ""
    optimized_code: str = ""
    
    def set_input_code(self, val: str):
        self.input_code = val
    
    def analyze_code(self):
        """Runs the complete analysis."""
        self.is_loading = True
        yield
        
        # 1. Basic Analysis (AST & Flake8)
        basic_res = analyze_code_basic(self.input_code)
        self.syntax_errors = basic_res["syntax_errors"]
        self.style_errors = basic_res["style_errors"]
        self.is_valid = basic_res["is_valid"]
        
        # 2. AI Analysis
        ai_res = analyze_code_with_ai(self.input_code)
        if "error" in ai_res:
             self.ai_issues = [ai_res["error"]]
             self.ai_optimizations = []
             self.time_complexity = "N/A"
             self.space_complexity = "N/A"
             self.optimized_code = ""
        else:
            self.ai_issues = ai_res.get("issues", [])
            self.ai_optimizations = ai_res.get("optimizations", [])
            self.time_complexity = ai_res.get("time_complexity", "")
            self.space_complexity = ai_res.get("space_complexity", "")
            self.optimized_code = ai_res.get("optimized_code", "")
            
        # 3. Save to history
        full_analysis = {
            "syntax_errors": self.syntax_errors,
            "style_errors": self.style_errors,
            "ai_issues": self.ai_issues,
            "ai_optimizations": self.ai_optimizations,
            "time_complexity": self.time_complexity,
            "space_complexity": self.space_complexity,
            "optimized_code": self.optimized_code,
        }
        add_to_history(self.input_code, full_analysis)
        
        self.is_loading = False

class HistoryState(AppState):
    history_items: List[HistoryItem] = []
    
    def load_history(self):
        raw_items = get_history()
        items = []
        for item in raw_items:
            ad = item.get("analysis", {})
            analysis = AnalysisResult(
                syntax_errors=ad.get("syntax_errors", []),
                style_errors=ad.get("style_errors", []),
                ai_issues=ad.get("ai_issues", []),
                ai_optimizations=ad.get("ai_optimizations", []),
                time_complexity=ad.get("time_complexity", ""),
                space_complexity=ad.get("space_complexity", ""),
                optimized_code=ad.get("optimized_code", "")
            )
            items.append(HistoryItem(
                id=item["id"],
                code=item["code"],
                timestamp=item.get("timestamp", 0),
                analysis=analysis
            ))
        self.history_items = items
        
    def delete_item(self, item_id: str):
        delete_history_item(item_id)
        self.load_history()

class ChatState(AppState):
    chat_history: List[ChatMessage] = []
    current_input: str = ""
    analyzed_code_context: str = ""
    
    def set_current_input(self, val: str):
        self.current_input = val
    
    def set_context(self, code: str):
        self.analyzed_code_context = code
        self.chat_history = []
        
    def send_message(self):
        if not self.current_input.strip():
            return
            
        user_msg = self.current_input
        self.chat_history.append(ChatMessage(role="user", content=user_msg))
        self.current_input = ""
        yield
        
        history_dicts = [{"role": msg.role, "content": msg.content} for msg in self.chat_history[:-1]]
        response = chat_with_aibot(self.analyzed_code_context, history_dicts, user_msg)
        self.chat_history.append(ChatMessage(role="assistant", content=response))
