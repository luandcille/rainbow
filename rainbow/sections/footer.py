import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button

def footer() -> rx.Component:
    return rx.flex(
        rx.heading("connect", size="7"),
        primary_button(
        button_texts="test",
        link="",
        ),
        primary_button(
            button_texts="test",
            link="",
        ),
        primary_button(
            button_texts="test",
            link="",
        ),
        # Style rx.flex
        direction="column",
        align="center",
        justify="center",
    ),
