import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button

def footer() -> rx.Component:
    return rx.flex(
        rx.container(
            rx.heading("connect", size="7", padding_bottom="5px", margin_top="40px", font_family="Didact Gothic", weight="medium"),
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
             padding_top="6px",
             padding_bottom="120px",
            ), 
            
            rx.flex(
                rx.image(src="images/lucille_logo.png", width="50px", height="50px", margin_bottom="5px"),
                rx.text("Made by Lucille Vigné", size="2", font_family="Didact Gothic", weight="regular"),
                rx.text("with rbnws 🌈", size="2", font_family="Didact Gothic", weight="regular"),
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