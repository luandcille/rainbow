import reflex as rx
from rxconfig import config

def primary_button(
    button_texts: list[str] = ["Button 1"], 
    link: str = "#",        
) -> rx.Component:
    return rx.link(
        rx.flex(
            rx.button(
                button_texts,
                color="black",
                background_color="white",
                radius="full",
                border="1px solid #000000",
                cursor="pointer",
                _hover={"opacity": 0.7},
            ),
            href=link,
        ), 
    ),

def secondary_button(label: str, on_click: callable = None):
    return rx.button(
        label,
        color_scheme="gray",
        size="md",
        variant="outline",
        border_radius="sm",
        on_click=on_click,
        _hover={"background_color": "gray.200"},
    )
