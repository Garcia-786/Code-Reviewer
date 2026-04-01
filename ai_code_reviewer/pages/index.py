import reflex as rx
from ai_code_reviewer.components.navbar import template


ACCENT         = "#6366F1"
ACCENT_SOFT    = "rgba(99,102,241,0.10)"
TEXT_PRIMARY   = "#F1F5F9"
TEXT_SECONDARY = "rgba(148,163,184,0.85)"
TEXT_MUTED     = "rgba(100,116,139,0.8)"
BORDER         = "rgba(255,255,255,0.08)"
BORDER_HOVER   = "rgba(99,102,241,0.45)"


def feature_card(number: str, title: str, desc: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(
                number,
                font_size="0.68rem",
                font_weight="700",
                letter_spacing="0.1em",
                color=ACCENT,
                margin_bottom="2",
            ),
            rx.text(
                title,
                font_size="0.95rem",
                font_weight="600",
                color=TEXT_PRIMARY,
                line_height="1.4",
                margin="10",
            ),
            rx.text(
                desc,
                font_size="0.82rem",
                color=TEXT_SECONDARY,
                line_height="1.65",
                margin="10",
            ),
            spacing="2",
            align_items="start",
            width="100%",
        ),
        border_radius="12px",
        padding="6",
        border=f"1px solid {BORDER}",
        background="rgba(255,255,255,0.025)",
        flex="1",
        min_width="210px",
        max_width="270px",
        transition="border-color 0.2s ease, background 0.2s ease",
        _hover={
            "border_color": BORDER_HOVER,
            "background": ACCENT_SOFT,
        },
    )


@rx.page(route="/", title="Home — AI Code Reviewer")
def index() -> rx.Component:
    return template(
        rx.vstack(

            rx.vstack(

                rx.heading(
                    "AI Code Review,",
                    rx.box(
                        rx.text.span(
                            "Done Instantly.",
                            style={
                                "background": f"linear-gradient(120deg, {ACCENT}, #A78BFA)",
                                "WebkitBackgroundClip": "text",
                                "WebkitTextFillColor": "transparent",
                            },
                        ),
                        display="block",
                    ),
                    size="8",
                    font_weight="700",
                    text_align="center",
                    color=TEXT_PRIMARY,
                    margin="10",
                ),

                rx.text(
                    "Analyze Python code for syntax errors, PEP 8 violations, "
                    "logic bugs, and complexity — in seconds.",
                    color=TEXT_SECONDARY,
                    text_align="center",
                    max_width="500px",
                    font_size="1rem",
                    line_height="1.8",
                ),

                # Buttons (FIXED SPACING)
                rx.flex(
                    rx.button(
                        "Start Analyzing",
                        on_click=rx.redirect("/analyzer"),
                        size="3",
                        background=ACCENT,
                        color="#FFFFFF",
                        border_radius="3px",
                        padding_x="20",
                        height="46px",
                        font_weight="600",
                        _hover={
                            "opacity": "0.9",
                            "transform": "translateY(-2px)",
                        },
                    ),
                    gap="5",
                    justify="center",
                    margin_top="6",
                ),

                spacing="8",
                align="center",
                padding_top="40",
                padding_bottom="40",
                width="100%",
            ),

            rx.flex(
                rx.box(height="1px", flex="1", background=BORDER),
                rx.text(
                    "FEATURES",
                    font_size="0.7rem",
                    font_weight="700",
                    letter_spacing="0.18em",
                    color=TEXT_MUTED,
                    padding_x="10",
                ),
                rx.box(height="1px", flex="1", background=BORDER),
                align="center",
                width="100%",
                margin_y="10",   
            ),

            rx.flex(
                feature_card(
                    "01",
                    "Syntax & Error Detection",
                    "Catches SyntaxErrors and undefined references via Python's AST.",
                ),
                feature_card(
                    "02",
                    "PEP 8 Style Analysis",
                    "Flags naming, indentation, and line-length issues with flake8.",
                ),
                feature_card(
                    "03",
                    "AI Suggestions",
                    "LLaMA 3.3 recommends cleaner patterns and smarter algorithms.",
                ),
                feature_card(
                    "04",
                    "Complexity Analysis",
                    "Auto-annotates Big-O time and space complexity.",
                ),
                gap="8",              
                flex_wrap="wrap",
                justify="center",
                width="100%",
                padding_top="6",
                padding_bottom="24",
            ),

            spacing="0",
            width="100%",
            max_width="1100px",
            margin_x="auto",
            align_items="center",
            padding_x="10",
        )
    )