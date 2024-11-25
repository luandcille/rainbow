import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button

def footer() -> rx.Component:
    return rx.flex(
        rx.container(
            rx.heading("connect", size="7"),
            rx.flex(
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
             width="400px",
             padding_bottom="120px",
            ), 
            
            rx.flex(
                rx.image(src="images/lucille_logo.png", width="50px", heigth="50px"),
                rx.text("Lorem Ipsum", size="2"),
                rx.text("Build By L with R", size="2"),
                width="100%",
                direction="column", 
                align="center",  
                justify="center",
            ),
        ),
        width="100%",
        direction="column", 
        align="center",  
        justify="center",  
    ),