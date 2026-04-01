import reflex as rx
from ai_code_reviewer.components.navbar import template

ACCENT = "#6366F1"


def step_item(num: str, title: str, desc: str) -> rx.Component:
    return rx.flex(
        rx.box(
            rx.text(num, color=ACCENT, font_weight="800", font_size="0.9rem"),
            background="rgba(108,99,255,0.1)",
            border="1px solid rgba(108,99,255,0.25)",
            border_radius="lg",
            width="40px",
            height="40px",
            display="flex",
            align_items="center",
            justify_content="center",
        ),
        rx.vstack(
            rx.text(title, color="white", font_weight="700"),
            rx.text(desc, color="rgba(255,255,255,0.5)", font_size="0.85rem"),
            align_items="start",
        ),
        gap="4",
        align="start",
        width="100%",
    )


@rx.page(route="/about", title="About — AI Code Reviewer")
def about() -> rx.Component:
    return template(
        rx.vstack(

            rx.heading("About This Project", size="8", color="white"),

            rx.text(
                "Understand how the AI Code Reviewer processes your code step by step.",
                color="rgba(255,255,255,0.5)",
            ),

            rx.divider(),

            rx.box(
                rx.vstack(
                    step_item("1", "Code Input", "User enters Python code."),
                    step_item("2", "Syntax Check", "AST validates structure."),
                    step_item("3", "Style Check", "flake8 analyzes formatting."),
                    step_item("4", "AI Analysis", "Groq model reviews logic and complexity."),
                    step_item("5", "Results", "Structured feedback is displayed and stored."),
                    spacing="5",
                    align_items="start",
                ),
                padding="6",
                border="1px solid rgba(108,99,255,0.2)",
                border_radius="xl",
                width="100%",
            ),

            spacing="6",
            width="100%",
        )
    )