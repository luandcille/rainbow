import reflex as rx
from rxconfig import config

def primary_button(
    button_text: list[str] = ["Button 1"], 
    link: str = "#",        
) -> rx.Component:
    return rx.link(
        rx.button(
            button_text,
            rx.icon("arrow-up-right", size=20 ,color="black", margin_left="-6px"),
            color="black",
            background_color="white",
            radius="full",
            border="1px solid #000000",
            cursor="pointer",
            _hover={"opacity": 0.7},
            padding_left="15px", 
            padding_right="10px",
        ),
        href=link,
    ),