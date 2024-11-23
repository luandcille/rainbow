import reflex as rx
from rxconfig import config

def body() -> rx.Component:
    return rx.section(
        rx.box( # Function of the anchor 
            id="body",
            padding_top="90px",
        ),
        rx.container(
            rx.image(src="/images/kwotes.png", width="100px", height="100px"),
            rx.link(
                rx.flex(
                    rx.heading("kwotes app", size="8", text_align="center"),
                    rx.icon("arrow-up-right", size=40),
                    href="www.google.com",
                ),  
            ),
            rx.button("Primary button"),
            rx.button("Secondary"),
            rx.text("There was a time"),
        ),
    ),
