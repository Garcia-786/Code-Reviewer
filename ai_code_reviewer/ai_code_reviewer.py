import reflex as rx
from dotenv import load_dotenv
load_dotenv()

from ai_code_reviewer.state import AppState
from ai_code_reviewer.pages import index
from ai_code_reviewer.pages import analyzer
from ai_code_reviewer.pages import history
from ai_code_reviewer.pages import aibot
from ai_code_reviewer.pages import about

style = {
    "font_family": "Inter, sans-serif",
}

style = {
    "font_family": "Inter, sans-serif",
    "background_color": "#0f172a",  # dark navy
    "color": "#e2e8f0",  # soft white text
}

app = rx.App(
    style=style,
    stylesheets=["/style.css"],
)