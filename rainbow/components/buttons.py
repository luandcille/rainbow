import reflex as rx
from rxconfig import config

def primary_button(label: str, on_click: callable = None):
    return rx.button(
        label,
        color_scheme="blue",
        size="lg",
        border_radius="md",
        on_click=on_click,
        _hover={"background_color": "blue.600"},
    )

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
