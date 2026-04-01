import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY");
    return Groq(api_key=api_key)

MODEL_NAME = "llama-3.3-70b-versatile"

def analyze_code_with_ai(code: str) -> dict:
    """Uses Groq to analyze code for optimizations, bugs, and complexities."""
    client = get_groq_client()
    if not client:
        return {"error": "GROQ_API_KEY is not set."}

    prompt = f"""
    You are an expert Python code reviewer. Analyze the following Python code and provide your response in JSON format.
    The JSON should have these keys:
    1. "issues": A list of logical bugs or potential errors (strings).
    2. "optimizations": A list of suggestions to improve readability and efficiency (strings).
    3. "time_complexity": The estimated time complexity (e.g., O(N)).
    4. "space_complexity": The estimated space complexity (e.g., O(1)).
    5. "optimized_code": A fully rewritten, improved version of the code snippet.

    Code to analyze:
    ```python
    {code}
    ```
    
    Return ONLY valid JSON. No markdown backticks around the json, no preamble.
    """

    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model=MODEL_NAME,
            temperature=0.2, 
        )
        
        response_text = completion.choices[0].message.content.strip()
        
        if response_text.startswith("```json"):
            response_text = response_text[7:]
        if response_text.startswith("```"):
            response_text = response_text[3:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
            
        return json.loads(response_text)
    except Exception as e:
        return {"error": str(e)}

def chat_with_aibot(code_context: str, history: list[dict], new_message: str) -> str:
    """Converses with the user about their code."""
    client = get_groq_client()
    if not client:
        return "GROQ_API_KEY is not set. Cannot use Aibot."

    messages = [
        {"role": "system", "content": f"You are an AI teaching assistant helping a student understand this specific python code:\n\n{code_context}\n\nBe concise, helpful, and teach concepts of OOP and DSA if applicable."}
    ]
    
    for msg in history:
        messages.append({"role": msg["role"], "content": msg["content"]})
        
    messages.append({"role": "user", "content": new_message})

    try:
        completion = client.chat.completions.create(
            messages=messages,
            model=MODEL_NAME,
            temperature=0.5,
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error connecting to AI: {str(e)}"
