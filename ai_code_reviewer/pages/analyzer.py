import reflex as rx
from ai_code_reviewer.components.navbar import template, section_card, badge
from ai_code_reviewer.state import AnalyzerState

ACCENT = "#6366F1"

def labeled_section(label: str, content: rx.Component) -> rx.Component:
    return rx.vstack(
        rx.text(
            label,
            color="rgba(255,255,255,0.3)",
            font_size="0.68rem",
            font_weight="700",
            letter_spacing="0.15em",
            margin_bottom="1",
        ),
        content,
        align_items="start",
        width="100%",
        spacing="2",
    )


def bullet_list(items, icon: str = "•", color: str = "#FC814A") -> rx.Component:
    return rx.cond(
        items.length() > 0,
        rx.vstack(
            rx.foreach(
                items,
                lambda item: rx.flex(
                    rx.text(icon, color=color, font_size="1rem", line_height="1.6", flex_shrink="0"),
                    rx.text(item, color="rgba(255,255,255,0.82)", font_size="0.875rem", line_height="1.65"),
                    gap="3",
                    align="start",
                    width="100%",
                )
            ),
            align_items="start",
            spacing="3",
            width="100%",
        ),
        rx.flex(
            rx.text("✓", color="#68D391", font_weight="700", font_size="1rem"),
            rx.text("All clear", color="#68D391", font_size="0.875rem"),
            gap="2",
            align="center",
            padding_y="2",
        )
    )


def complexity_badge(label: str, value: str, bg: str, fg: str) -> rx.Component:
    return rx.box(
        rx.vstack(
            rx.text(label, color="rgba(255,255,255,0.45)", font_size="0.68rem", font_weight="700", letter_spacing="0.1em"),
            rx.text(value, color=fg, font_size="1.5rem", font_weight="bold", letter_spacing="-0.02em"),
            spacing="1",
            align_items="start",
        ),
        background=bg,
        border=f"1px solid {fg}33",
        border_radius="xl",
        padding_x="6",
        padding_y="4",
        flex="1",
        min_width="160px",
    )


@rx.page(route="/analyzer", title="Analyzer — AI Code Reviewer")
def analyzer() -> rx.Component:
    return template(
        rx.vstack(
            rx.vstack(
                rx.heading("Code Analyzer", size="8", color="white", font_weight="bold"),
                rx.text(
                    "Paste Python code below and receive an instant, multi-dimensional AI review.",
                    color="rgba(255,255,255,0.45)",
                    font_size="0.95rem",
                ),
                spacing="2",
                align_items="start",
                width="100%",
            ),

            rx.divider(border_color="rgba(108,99,255,0.15)", margin_y="2"),

            labeled_section("YOUR PYTHON CODE",
                rx.box(
                    rx.text_area(
                        placeholder="# Paste your Python code here...\ndef hello_world():\n    print('Hello, World!')",
                        value=AnalyzerState.input_code,
                        on_change=AnalyzerState.set_input_code,
                        height="300px",
                        width="100%",
                        font_family="'JetBrains Mono', 'Fira Code', monospace",
                        font_size="0.875rem",
                        line_height="1.6",
                        background="rgba(0,0,0,0.35)",
                        border="1px solid rgba(108,99,255,0.25)",
                        border_radius="xl",
                        color="rgba(255,255,255,0.9)",
                        padding="5",
                        resize="vertical",
                        _focus={
                            "border_color": ACCENT,
                            "outline": "none",
                            "box_shadow": "0 0 0 3px rgba(108,99,255,0.2)",
                        },
                        _placeholder={"color": "rgba(255,255,255,0.15)"},
                    ),
                    width="100%",
                ),
            ),

            rx.button(
                rx.cond(
                    AnalyzerState.is_loading,
                    rx.flex(
                        rx.spinner(size="2", color="white"),
                        rx.text("Analyzing code…", margin_left="3"),
                        align="center",
                    ),
                    rx.flex(rx.text("⚡"), rx.text(" Run Full Analysis", margin_left="2"), align="center"),
                ),
                on_click=AnalyzerState.analyze_code,
                loading=AnalyzerState.is_loading,
                size="3",
                width="100%",
                cursor="pointer",
                background=f"linear-gradient(135deg, {ACCENT}, #A78BFA)",
                color="white",
                border_radius="xl",
                padding_y="5",
                font_weight="700",
                font_size="1rem",
                letter_spacing="0.01em",
                _hover={"opacity": "0.88"},
                transition="all 0.2s ease",
            ),

            rx.cond(
                AnalyzerState.time_complexity != "",
                rx.vstack(

                    rx.flex(
                        rx.divider(border_color="rgba(108,99,255,0.15)", flex="1"),
                        rx.text("ANALYSIS RESULTS", color="rgba(255,255,255,0.25)", font_size="0.68rem", font_weight="700", letter_spacing="0.18em", padding_x="5"),
                        rx.divider(border_color="rgba(108,99,255,0.15)", flex="1"),
                        align="center",
                        width="100%",
                    ),

                    # Complexity strip
                    rx.flex(
                        complexity_badge("TIME COMPLEXITY", AnalyzerState.time_complexity, "rgba(183,148,244,0.08)", "#B794F4"),
                        complexity_badge("SPACE COMPLEXITY", AnalyzerState.space_complexity, "rgba(104,211,145,0.08)", "#68D391"),
                        gap="4",
                        flex_wrap="wrap",
                        width="100%",
                    ),

                    # Error & style grid
                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.text("🔴", font_size="1rem"),
                                rx.text("Syntax Errors", color="white", font_weight="700", font_size="0.95rem"),
                                gap="2", align="center", margin_bottom="4",
                            ),
                            bullet_list(AnalyzerState.syntax_errors, "✗", "#FC8181"),
                            background="rgba(252,129,129,0.05)",
                            border="1px solid rgba(252,129,129,0.2)",
                            border_radius="xl",
                            padding="5",
                            flex="1",
                            min_width="280px",
                        ),
                        rx.box(
                            rx.flex(
                                rx.text("🟡", font_size="1rem"),
                                rx.text("PEP8 Style Issues", color="white", font_weight="700", font_size="0.95rem"),
                                gap="2", align="center", margin_bottom="4",
                            ),
                            bullet_list(AnalyzerState.style_errors, "!", "#F6AD55"),
                            background="rgba(246,173,85,0.05)",
                            border="1px solid rgba(246,173,85,0.2)",
                            border_radius="xl",
                            padding="5",
                            flex="1",
                            min_width="280px",
                        ),
                        gap="5",
                        flex_wrap="wrap",
                        width="100%",
                    ),

                    rx.flex(
                        rx.box(
                            rx.flex(
                                rx.text("🤖", font_size="1rem"),
                                rx.text("Logical Issues", color="white", font_weight="700", font_size="0.95rem"),
                                gap="2", align="center", margin_bottom="4",
                            ),
                            bullet_list(AnalyzerState.ai_issues, "→", "#FC8181"),
                            background="rgba(252,129,129,0.04)",
                            border="1px solid rgba(108,99,255,0.18)",
                            border_radius="xl",
                            padding="5",
                            flex="1",
                            min_width="280px",
                        ),
                        rx.box(
                            rx.flex(
                                rx.text("💡", font_size="1rem"),
                                rx.text("Optimization Suggestions", color="white", font_weight="700", font_size="0.95rem"),
                                gap="2", align="center", margin_bottom="4",
                            ),
                            bullet_list(AnalyzerState.ai_optimizations, "→", "#68D391"),
                            background="rgba(104,211,145,0.04)",
                            border="1px solid rgba(108,99,255,0.18)",
                            border_radius="xl",
                            padding="5",
                            flex="1",
                            min_width="280px",
                        ),
                        gap="5",
                        flex_wrap="wrap",
                        width="100%",
                    ),

                    rx.cond(
                        AnalyzerState.optimized_code != "",
                        rx.vstack(
                            rx.flex(
                                rx.divider(border_color="rgba(108,99,255,0.15)", flex="1"),
                                rx.text("CODE COMPARISON", color="rgba(255,255,255,0.25)", font_size="0.68rem", font_weight="700", letter_spacing="0.18em", padding_x="5"),
                                rx.divider(border_color="rgba(108,99,255,0.15)", flex="1"),
                                align="center",
                                width="100%",
                            ),
                            rx.flex(
                                rx.box(
                                    rx.flex(
                                        rx.text("Original", color="rgba(255,255,255,0.5)", font_size="0.8rem", font_weight="600"),
                                        badge("BEFORE", "red"),
                                        justify="between",
                                        align="center",
                                        margin_bottom="3",
                                    ),
                                    rx.code_block(AnalyzerState.input_code, language="python", show_line_numbers=True, wrap_long_lines=True, width="100%"),
                                    flex="1",
                                    min_width="300px",
                                ),
                                rx.box(
                                    rx.flex(
                                        rx.text("Optimized", color="rgba(255,255,255,0.5)", font_size="0.8rem", font_weight="600"),
                                        badge("AFTER", "green"),
                                        justify="between",
                                        align="center",
                                        margin_bottom="3",
                                    ),
                                    rx.code_block(AnalyzerState.optimized_code, language="python", show_line_numbers=True, wrap_long_lines=True, width="100%"),
                                    flex="1",
                                    min_width="300px",
                                ),
                                gap="5",
                                flex_wrap="wrap",
                                width="100%",
                            ),
                            spacing="5",
                            width="100%",
                            align_items="start",
                        ),
                        rx.box(),
                    ),

                    spacing="6",
                    width="100%",
                    align_items="start",
                ),
                rx.box(),
            ),

            spacing="6",
            width="100%",
            align_items="start",
            padding_bottom="12",
        )
    )
