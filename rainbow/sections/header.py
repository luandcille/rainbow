import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button, secondary_button

def header() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.color_mode.button(position="top-right"),  # Light/Dark Mode
            rx.image(src="images/hello_lu.png", width="200px", height="200px"),
            rx.heading("HELLO, I AM LUCILLE", size="4", font_family="Didact Gothic", weight="light", padding_bottom="5px", padding_top="10px", text_align="center", letter_spacing="2px"),
            rx.text("A Creative and Visionary", font_family="Didact Gothic", weight="bold", size="7", text_align="center", padding_bottom="-5px"),
            rx.text("Product Owner", size="7", text_align="center", margin_top="-4px", font_family="Didact Gothic", weight="bold", padding_bottom="15px"),
            secondary_button(
                button_text="HIRE ME",
                link="https://www.linkedin.com/in/lucillevigne", 
                ),
            rx.box(
                rx.link(
                    rx.icon(
                        "circle-chevron-down",
                        stroke_width=1,
                        margin_top="100px",
                        margin_bottom="100px",
                        _hover=rx.color_mode_cond(
                            light={"color": "#000000", "opacity": 0.7}, # Light mode styles
                            dark={"color": "#ffffff", "opacity": 0.7}, # Dark mode styles
                        ),
                    ),
                    href="#body", # Ensure this targets the body section
                    cursor="pointer",
                    color="inherit",
                ),
            ),
            # rx.flex style
            width="100%",
            direction="column",
            align="center",
            justify="center",
            padding_top="100px", 
        ),
    ),