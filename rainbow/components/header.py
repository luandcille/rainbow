# ------------------------------------
# ℹ️ COMPONENT: HEADER
# ------------------------------------
# This file defines the main header section of the site, including:
# - Dark/light mode toggle
# - Profile image and intro text
# - CTA button ("Hire Me")
# - Scroll-down anchor icon


# --- 📦 Imports ---
import reflex as rx
from rainbow.components.buttons import secondary_button


# --- 🧠 Header Component ---
def header() -> rx.Component:
    return rx.section(
        rx.flex(
            # 🌗 Dark/Light toggle
            rx.color_mode.button(position="top-right"),

            # 👋 Profile image
            rx.image(
                src="images/hello_lu.png",
                width="200px",
                height="200px",
            ),

            # 📢 Headings
            rx.heading(
                "HELLO, I AM LUCILLE",
                size="4",
                font_family="Didact Gothic",
                weight="light",
                padding_bottom="5px",
                padding_top="10px",
                text_align="center",
                letter_spacing="2px",
            ),
            rx.text(
                "A Creative and Visionary",
                font_family="Didact Gothic",
                weight="bold",
                size="7",
                text_align="center",
                padding_bottom="-5px",
            ),
            rx.text(
                "Product Owner",
                size="7",
                text_align="center",
                margin_top="-4px",
                font_family="Didact Gothic",
                weight="bold",
                padding_bottom="15px",
            ),

            # 💼 CTA Button
            secondary_button(
                button_text="HIRE ME",
                link="https://www.linkedin.com/in/lucillevigne",
            ),

            # 🔽 Scroll-down icon link
            rx.box(
                rx.link(
                    rx.icon(
                        "circle-chevron-down",
                        stroke_width=1,
                        margin_top="100px",
                        margin_bottom="100px",
                        class_name="transition-transform duration-300 ease-in-out hover:translate-y-1",
                        _hover=rx.color_mode_cond(
                            light={"color": "#000000", "opacity": 0.7},
                            dark={"color": "#ffffff", "opacity": 0.7},
                        ),
                    ),
                    href="#body",
                    cursor="pointer",
                    color="inherit",
                ),
            ),

            # 📐 Layout
            width="100%",
            direction="column",
            align="center",
            justify="center",
            padding_top="100px",
        ),
    )
