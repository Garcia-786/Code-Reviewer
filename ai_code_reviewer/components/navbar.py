import reflex as rx
from ai_code_reviewer.components.footer import footer

# Theme colors
NAV_BG = "rgba(15, 23, 42, 0.95)"
ACCENT = "#6366F1"


def navbar() -> rx.Component:
    return rx.box(
        rx.flex(
            # Logo section
            rx.flex(
                rx.heading(
                    "Code",
                    rx.text.span("AI", color=ACCENT),
                    " Reviewer",
                    size="6",
                    color="#E2E8F0",
                    font_weight="700",
                    letter_spacing="-0.02em",
                ),
                align="center",
                justify="center",
                padding_x="4",
            ),

            # Nav links section
            rx.flex(
                *[
                    rx.link(
                        label,
                        href=href,
                        color="rgba(226,232,240,0.75)",
                        font_size="0.95rem",
                        font_weight="500",
                        padding_x="5",
                        padding_y="3",
                        border_radius="lg",
                        transition="all 0.2s ease",
                        white_space="nowrap",
                        _hover={
                            "color": "#FFFFFF",
                            "background": "rgba(99,102,241,0.18)",
                        },
                    )
                    for label, href in [
                        ("Home", "/"),
                        ("Analyzer", "/analyzer"),
                        ("History", "/history"),
                        ("AI Bot", "/aibot"),
                        ("About", "/about"),
                    ]
                ],
                gap="4",  # FIXED spacing
                align="center",
                justify="center",
            ),

            justify="between",
            align="center",
            width="100%",
            max_width="1400px",
            margin="0 auto",
            padding_x="10",
        ),

        background=NAV_BG,
        border_bottom="1px solid rgba(99,102,241,0.2)",
        backdrop_filter="blur(24px)",
        padding_y="5",
        position="sticky",
        top="0",
        z_index="100",
        width="100%",
        min_height="72px",
    )


def section_card(
    title: str,
    content: rx.Component,
    icon: str = "",
    color: str = ACCENT
) -> rx.Component:
    return rx.box(
        rx.flex(
            rx.flex(
                rx.text(
                    icon,
                    font_size="1.5rem",
                    margin_right="3" if icon else "0",
                ) if icon else rx.box(),
                rx.heading(
                    title,
                    size="4",
                    color="#F8FAFC",
                    margin="0",
                ),
                align="center",
                gap="3" if icon else "0",
                margin_bottom="4",
                width="100%",
            ),
            rx.box(
                content,
                width="100%",
            ),
            direction="column",
            spacing="4",
            width="100%",
        ),
        border_radius="16px",
        padding="6",
        width="100%",
        border="1px solid rgba(99,102,241,0.15)",
        background="rgba(23, 27, 40, 0.85)",
        _hover={
            "border_color": "rgba(108,99,255,0.45)",
            "transform": "scale(1.02)",
            "box_shadow": "0 8px 20px rgba(0,0,0,0.15)",
        },
    )


def badge(text: str, color: str = "blue") -> rx.Component:
    colors = {
        "blue": ("rgba(59,130,246,0.15)", "#3B82F6"),
        "red": ("rgba(239,68,68,0.15)", "#EF4444"),
        "green": ("rgba(34,197,94,0.15)", "#22C55E"),
        "purple": ("rgba(147,51,234,0.15)", "#9333EA"),
        "orange": ("rgba(249,115,22,0.15)", "#F97316"),
        "slate": ("rgba(71,85,105,0.15)", "#475569"),
    }

    bg, fg = colors.get(color, colors["blue"])

    return rx.box(
        rx.text(
            text,
            color=fg,
            font_size="0.75rem",
            font_weight="600",
            margin="0",
        ),
        background=bg,
        border=f"1px solid {fg}30",
        border_radius="full",
        padding_x="3.5",
        padding_y="1.5",
        margin_right="2",
    )


def template(page_content: rx.Component) -> rx.Component:
    return rx.box(
        rx.box(class_name="blob blob-1"),
        rx.box(class_name="blob blob-2"),

        navbar(),

        rx.box(
            page_content,
            padding_x="8",
            padding_y="12",
            padding_top="14",
            max_width="1400px",
            margin="0 auto",
            min_height="80vh",
            width="100%",
        ),

        footer(),

        background="linear-gradient(135deg, #0F0F23 0%, #1A1A2E 50%, #0F0F23 100%)",
        min_height="100vh",
        color="#E2E8F0",
        font_family="'Inter', sans-serif",
        position="relative",
        overflow="hidden",
    )