import reflex as rx
from ai_code_reviewer.components.navbar import template
from ai_code_reviewer.state import HistoryState, HistoryItem

ACCENT = "#6366F1"


def history_card(item: HistoryItem) -> rx.Component:
    has_errors = item.analysis.syntax_errors.length() > 0
    return rx.box(
        rx.flex(
            rx.flex(
                rx.box(
                    width="8px", height="8px",
                    background=rx.cond(has_errors, "#FC8181", "#68D391"),
                    border_radius="full",
                    margin_top="6px",
                    flex_shrink="0",
                    box_shadow=rx.cond(has_errors, "0 0 8px rgba(252,129,129,0.5)", "0 0 8px rgba(104,211,145,0.5)"),
                ),
                rx.vstack(
                    rx.cond(
                        has_errors,
                        rx.text("Issues Detected", color="#FC8181", font_size="0.72rem", font_weight="700", letter_spacing="0.05em"),
                        rx.text("Clean Code", color="#68D391", font_size="0.72rem", font_weight="700", letter_spacing="0.05em"),
                    ),
                    rx.text("Python Code Review", color="white", font_weight="600", font_size="1rem"),
                    spacing="0",
                    align_items="start",
                ),
                gap="3",
                align="start",
            ),
            rx.button(
                "Delete",
                on_click=lambda: HistoryState.delete_item(item.id),
                size="1",
                cursor="pointer",
                variant="ghost",
                color="rgba(252,129,129,0.7)",
                border="1px solid rgba(252,129,129,0.2)",
                border_radius="lg",
                padding_x="3",
                _hover={"background": "rgba(252,129,129,0.1)", "border_color": "#FC8181", "color": "#FC8181"},
                transition="all 0.2s ease",
            ),
            justify="between",
            align="center",
            margin_bottom="4",
        ),
        rx.box(
            rx.code_block(
                item.code,
                language="python",
                show_line_numbers=True,
                wrap_long_lines=True,
                max_height="180px",
                overflow_y="auto",
                width="100%",
                font_size="0.8rem",
            ),
            border_radius="lg",
            overflow="hidden",
            border="1px solid rgba(108,99,255,0.12)",
        ),

        background="rgba(255,255,255,0.03)",
        class_name="glass-card",
        border_radius="2xl",
        padding="6",
        width="100%",
        transition="all 0.2s ease",
        _hover={
            "border_color": "rgba(108,99,255,0.4)",
            "box_shadow": "0 4px 24px rgba(0,0,0,0.35)",
            "background": "rgba(255,255,255,0.04)",
        },
    )


@rx.page(route="/history", title="History — AI Code Reviewer", on_load=HistoryState.load_history)
def history() -> rx.Component:
    return template(
        rx.vstack(

            rx.vstack(
                rx.heading("Analysis History", size="8", color="white", font_weight="bold"),
                rx.text("All your previous Python code reviews, stored locally.", color="rgba(255,255,255,0.45)", font_size="0.95rem"),
                spacing="2",
                align_items="start",
                width="100%",
            ),

            rx.divider(border_color="rgba(108,99,255,0.15)", margin_y="2"),

            rx.cond(
                HistoryState.history_items.length() == 0,
                rx.flex(
                    rx.vstack(
                        rx.text("📭", font_size="3.5rem"),
                        rx.heading("No reviews yet", size="5", color="rgba(255,255,255,0.55)"),
                        rx.text("Analyze some code first and it'll appear here.", color="rgba(255,255,255,0.3)", font_size="0.9rem"),
                        rx.button(
                            "Go to Analyzer →",
                            on_click=rx.redirect("/analyzer"),
                            size="2",
                            cursor="pointer",
                            background=f"linear-gradient(135deg, {ACCENT}, #A78BFA)",
                            color="white",
                            border_radius="xl",
                            padding_x="6",
                            margin_top="3",
                            font_weight="600",
                            _hover={"opacity": "0.85"},
                        ),
                        align="center",
                        spacing="3",
                        padding_y="20",
                    ),
                    justify="center",
                    width="100%",
                ),
                rx.vstack(
                    rx.foreach(HistoryState.history_items, history_card),
                    width="100%",
                    spacing="5",
                    align_items="start",
                ),
            ),

            spacing="5",
            align_items="start",
            width="100%",
            padding_bottom="12",
        )
    )
