import os
import json
import uuid

HISTORY_FILE = "review_history.json"

def get_history() -> list[dict]:
    """Returns the review history from the local JSON file."""
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_history(history: list[dict]):
    """Saves the history to the local JSON file."""
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

def add_to_history(code: str, analysis: dict):
    """Adds a new code analysis block to the history."""
    history = get_history()
    entry = {
        "id": str(uuid.uuid4()),
        "code": code,
        "analysis": analysis,
        "timestamp": os.path.getmtime(HISTORY_FILE) if os.path.exists(HISTORY_FILE) else 0 # simple placeholder
    }
    history.insert(0, entry)
    save_history(history)

def delete_history_item(item_id: str):
    """Deletes an item from the history by ID."""
    history = get_history()
    history = [item for item in history if item["id"] != item_id]
    save_history(history)
