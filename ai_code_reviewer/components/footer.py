import reflex as rx

def footer() -> rx.Component:
    return rx.box(
        rx.vstack(

            rx.divider(border_color="rgba(99,102,241,0.15)"),

            rx.flex(

                rx.vstack(
                    rx.flex(
                        rx.text("⚡", font_size="1.2rem"),
                        rx.heading(
                            "CodeAI Reviewer",
                            size="4",
                            color="#E2E8F0",
                            font_weight="600",
                        ),
                        align="center",
                        gap="2",
                    ),

                    rx.text(
                        "Empowering developers with instant, intelligent Python code analysis.",
                        color="rgba(226,232,240,0.6)",
                        font_size="0.85rem",
                        max_width="320px",
                        line_height="1.6",
                    ),

                    align_items="start",
                    spacing="3",
                ),

                rx.flex(

                    rx.vstack(
                        rx.text("Product", font_weight="600", font_size="0.9rem"),
                        rx.link("Analyzer", href="/analyzer"),
                        rx.link("History", href="/history"),
                        rx.link("AI Bot", href="/aibot"),
                        spacing="2",
                        align_items="start",
                    ),

                    rx.vstack(
                        rx.text("Resources", font_weight="600", font_size="0.9rem"),
                        rx.link("About", href="/about"),
                        rx.link("Docs", href="#"),
                        spacing="2",
                        align_items="start",
                    ),

                    gap="16",  
                ),

                justify="between",
                align="start",
                width="100%",
                flex_wrap="wrap",
                gap="10",
                padding_y="10",
            ),

            rx.flex(
                rx.text(
                    "© 2026 CodeAI Reviewer",
                    color="rgba(255,255,255,0.4)",
                    font_size="0.75rem",
                ),

                rx.flex(
                    rx.link("Privacy", href="#"),
                    rx.link("Terms", href="#"),
                    gap="5",
                ),

                justify="between",
                width="100%",
                padding_top="6",
                padding_bottom="8",
                border_top="1px solid rgba(255,255,255,0.08)",
            ),

            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding_x="8",
        ),

        width="100%",
        background="rgba(10, 10, 20, 0.5)",
        margin_top="16",  
    )