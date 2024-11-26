import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button

def footer() -> rx.Component:
    return rx.flex(
        rx.container(
            rx.heading("connect", size="8", padding_bottom="5px", margin_top="60px"),
            rx.flex(
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
                link="https://www.behance.net/sonolucilla",
                ),
             width="380px",
             spacing="1",
             padding_bottom="120px",
            ), 
            
            rx.flex(
                rx.image(src="images/lucille_logo.png", width="50px", heigth="50px"),
                rx.text("By Lucille Vigné", size="2"),
                rx.text("Built with 🌈 & Reflex", size="2"),
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