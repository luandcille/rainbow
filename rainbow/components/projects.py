import reflex as rx
from rxconfig import config

def project_container(
    logo_src: str = "/images/default.png",
    title: str = "Default Title",          
    description: str = "Default description text goes here.", 
    link: str = "#",                     
    button_text_1: list[str] = ["Button 1"], 
    button_text_2: list[str] = ["Button 2"], 
) -> rx.Component:
    return rx.flex(
        rx.container(
                rx.image(src=logo_src, width="65px", height="65px", margin_bottom="10px"),
                rx.link(
                    rx.flex(
                        rx.heading(title, size="8", text_align="center", margin_bottom="2px", font_family="Didact Gothic", weight="regular"),
                        rx.icon("arrow-up-right", stroke_width=1.4, size=30, margin_bottom="2px"),
                        _hover=rx.color_mode_cond(
                            light={"opacity": 0.9,"color": "#333333"}, 
                            dark={"opacity": 0.7, "color": "#FFFFFF"},
                        ),
                    ),
                    href=link, 
                    text_decoration="none",
                    color="inherit",
                ),
                rx.flex(
                    rx.button(button_text_1, font_family="Didact Gothic", font_weight="600", radius="full", color="black", background_color="white", border="1px solid #000000", size="1", padding_left="10px", padding_right="10px", margin_top="5px", margin_bottom="5px"),
                    rx.button(button_text_2, font_family="Didact Gothic", font_weight="600", radius="full", color="black", background_color="white", border="1px solid #000000", size="1", padding_left="10px", padding_right="10px", margin_top="5px", margin_bottom="5px"),
                    spacing="1",
                ),
                rx.text(description, size="4", font_family="Didact Gothic", weight="regular", margin_top="3px"),
            width="400px",
        ),
        padding_top="10px",
        padding_bottom="50px",
    ),