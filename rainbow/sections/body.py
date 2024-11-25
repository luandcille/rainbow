import reflex as rx
from rxconfig import config

from rainbow.components.projects import project_container

def body() -> rx.Component:
    return rx.flex(
        rx.box( # Function of the anchor 
            id="body",
            padding_top="100px",
        ),
        project_container(
            logo_src="/images/la_zebrelle.png", 
            title="la zébrelle", 
            description="Kwotes offers a vast collection of inspiring quotes from diverse sources. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away.", 
            link="", 
            button_texts=["Test"],
        ),  
        project_container(
            logo_src="/images/la_zebrelle.png", 
            title="la zébrelle", 
            description="Kwotes offers a vast collection of inspiring quotes from diverse sources. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away.", 
            link="", 
            button_texts=["Test"],
        ),  
        project_container(
            logo_src="/images/la_zebrelle.png", 
            title="la zébrelle", 
            description="Kwotes offers a vast collection of inspiring quotes from diverse sources. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away.", 
            link="", 
            button_texts=["Test"],
        ),  
        project_container(
            logo_src="/images/la_zebrelle.png", 
            title="la zébrelle", 
            description="Kwotes offers a vast collection of inspiring quotes from diverse sources. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away.", 
            link="", 
            button_texts=["Test"],
        ),
        width="100%",
        direction="column",
        align="center",
        justify="center", 
   ),          