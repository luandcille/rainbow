# ------------------------------------
# ℹ️ COMPONENT: FOOTER
# ------------------------------------
# This file defines the footer section with:
# - A heading ("connect")
# - A row of custom buttons (CV, LinkedIn, Behance)
# - A closing signature with logo and credits


# --- 📦 Imports ---
import reflex as rx
from rainbow.components.buttons import primary_button


# --- 🔻 Footer Component ---
def footer() -> rx.Component:
    return rx.flex(
        rx.container(
            # Heading
            rx.heading(
                "connect",
                size="7",
                padding_bottom="5px",
                font_family="Didact Gothic",
                weight="medium",
            ),

            # Social Buttons
            rx.flex(
                primary_button(
                    button_text="shop",
                    link="https://lucillevigne.bigcartel.com",
                ),
                primary_button(
                    button_text="cv.read",
                    link="https://read.cv/lucillevigne",
                ),
                primary_button(
                    button_text="linkedin",
                    link="https://www.linkedin.com/in/lucillevigne",
                ),
                primary_button(
                    button_text="behance",
                    link="https://www.behance.net/lucillevigne",
                ),
                width="380px",
                spacing="1",
                # padding_top="6px",
                padding_bottom="100px",
            ),

            # Signature
            rx.flex(
                rx.image(
                    src="images/lucille_logo.png",
                    width="50px",
                    height="50px",
                    margin_bottom="5px",
                ),
                rx.text(
                    "Coded by Lucille Vigné",
                    size="2",
                    font_family="Didact Gothic",
                    weight="regular",
                ),
                rx.text(
                    "with rbnws 🌈",
                    size="2",
                    font_family="Didact Gothic",
                    weight="regular",
                ),
                width="100%",
                direction="column",
                align="center",
                justify="center",
                padding_bottom="15px",
            ),
        ),
        width="100%",
        direction="column",
        align="center",
        justify="center",
    )
