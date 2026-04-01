import reflex as rx
from ai_code_reviewer.components.navbar import template
from ai_code_reviewer.state import ChatState, ChatMessage

ACCENT = "#6366F1"


def chat_bubble(msg: ChatMessage) -> rx.Component:
    is_user = msg.role == "user"
    return rx.flex(
        rx.vstack(
            rx.text(
                rx.cond(is_user, "You", "✨ Aibot"),
                font_size="0.68rem",
                font_weight="700",
                letter_spacing="0.05em",
                color=rx.cond(is_user, "rgba(167,139,250,0.7)", "rgba(104,211,145,0.7)"),
                margin_bottom="1",
            ),
            rx.text(
                msg.content,
                font_size="0.9rem",
                line_height="1.7",
                color="rgba(255,255,255,0.88)",
                style={"white_space": "pre-wrap"},
            ),
            align_items=rx.cond(is_user, "end", "start"),
            background=rx.cond(
                is_user,
                "linear-gradient(135deg, rgba(108,99,255,0.2), rgba(167,139,250,0.15))",
                "rgba(255,255,255,0.04)",
            ),
            class_name="glass-card",
            border_radius=rx.cond(is_user, "xl xl 4px xl", "xl xl xl 4px"),
            padding_x="5",
            padding_y="4",
            max_width="72%",
            spacing="1",
        ),
        justify=rx.cond(is_user, "end", "start"),
        width="100%",
    )


@rx.page(route="/aibot", title="Aibot — AI Code Reviewer")
def aibot() -> rx.Component:
    return template(
        rx.vstack(

            rx.vstack(
                rx.heading("AI BOT", size="8", color="white", font_weight="800"),
                rx.text(
                    "Your AI teaching assistant — ask anything about code",
                    color="rgba(255,255,255,0.45)",
                    font_size="0.95rem",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),

            rx.divider(border_color="rgba(108,99,255,0.15)", margin_y="2"),

            rx.vstack(
                rx.text("CODE CONTEXT", color="rgba(255,255,255,0.3)", font_size="0.68rem", font_weight="700", letter_spacing="0.15em"),
                rx.text_area(
                    placeholder="Paste the Python code you want to discuss with Aibot…",
                    value=ChatState.analyzed_code_context,
                    on_change=ChatState.set_context,
                    height="140px",
                    width="100%",
                    font_family="'JetBrains Mono', monospace",
                    font_size="0.825rem",
                    line_height="1.6",
                    background="rgba(0,0,0,0.3)",
                    border="1px solid rgba(108,99,255,0.22)",
                    border_radius="xl",
                    color="rgba(255,255,255,0.85)",
                    padding="4",
                    _focus={"border_color": ACCENT, "outline": "none", "box_shadow": "0 0 0 3px rgba(108,99,255,0.18)"},
                    _placeholder={"color": "rgba(255,255,255,0.15)"},
                ),
                spacing="2",
                width="100%",
            ),

            rx.box(
                rx.cond(
                    ChatState.chat_history.length() == 0,
                    rx.flex(
                        rx.vstack(
                            rx.text("💬", font_size="2.5rem"),
                            rx.text("No messages yet", color="rgba(255,255,255,0.3)", font_size="0.9rem", font_weight="600"),
                            rx.text("Set a code context above and start chatting!", color="rgba(255,255,255,0.2)", font_size="0.8rem"),
                            align="center",
                            spacing="2",
                        ),
                        justify="center",
                        align="center",
                        height="100%",
                    ),
                    rx.vstack(
                        rx.foreach(ChatState.chat_history, chat_bubble),
                        width="100%",
                        align_items="stretch",
                        spacing="4",
                    ),
                ),
                background="rgba(0,0,0,0.2)",
                border="1px solid rgba(108,99,255,0.12)",
                border_radius="xl",
                padding="5",
                height="420px",
                overflow_y="auto",
                width="100%",
            ),

            rx.flex(
                rx.input(
                    placeholder="Ask about the code, OOP concepts, time complexity, DSA algorithms…",
                    value=ChatState.current_input,
                    on_change=ChatState.set_current_input,
                    flex="1",
                    size="3",
                    background="rgba(255,255,255,0.05)",
                    border="1px solid rgba(108,99,255,0.22)",
                    border_radius="xl",
                    color="white",
                    padding_x="4",
                    _focus={"border_color": ACCENT, "outline": "none"},
                    _placeholder={"color": "rgba(255,255,255,0.22)"},
                ),
                rx.button(
                    "Send ➤",
                    on_click=ChatState.send_message,
                    size="3",
                    cursor="pointer",
                    background=f"linear-gradient(135deg, {ACCENT}, #A78BFA)",
                    color="white",
                    border_radius="xl",
                    font_weight="700",
                    padding_x="6",
                    _hover={"opacity": "0.85"},
                    transition="all 0.2s ease",
                ),
                gap="3",
                width="100%",
                align="center",
            ),

            spacing="5",
            width="100%",
            align_items="start",
            padding_bottom="12",
        )
    )
