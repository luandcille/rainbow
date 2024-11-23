import reflex as rx
from rxconfig import config

def header() -> rx.Component:
    return rx.section(
        rx.flex(
            rx.color_mode.button(position="top-right"),  # Light/Dark Mode
            rx.image(src="images/hello_lu.png", width="150px", height="150px"),
            rx.heading("HELLO, I AM LUCILLE", size="2", paddinfg_bottom="5px", padding_top="10px", text_align="center", letter_spacing="0.5px"),
            rx.text("A Creative and Visionary", size="6", text_align="center", font_weight="bold", padding_bottom="-5px"),
            rx.text("Product Owner", size="6", text_align="center", margin_top="-4px", font_weight="bold", padding_bottom="15px"),
            rx.box(
                rx.link(
                    rx.button(
                        "HIRE ME",
                        color="black",
                        background_color="white",
                        radius="full",
                        border="1px solid #000000",
                        cursor="pointer",
                        _hover={"opacity": 0.8},
                    ),
                    href="https://www.linkedin.com/in/lucillevigne/",
                ),
            ),  
            rx.box(
                rx.link(
                    rx.icon(
                        "circle-chevron-down",
                        stroke_width=1.2,
                        margin_top="50px",
                        _hover=rx.color_mode_cond(
                            light={"color": "#333333", "opacity": 0.9}, # Light mode styles
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
            padding_top="150px", 
        ),
    ),