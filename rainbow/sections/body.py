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
            logo_src="/images/aesthetic.png", 
            title="aesthetic", 
            description=" Make your Notion titles pop with that creative extension. Customize your headings like never before, adding a unique touch to your digital space", 
            link="https://www.aesthetics.so", 
            button_text_1=["founder"],
            button_text_2=["extension"],
        ),  
        project_container(
            logo_src="/images/kwotes.png", 
            title="kwotes app", 
            description="Kwotes offers a vast collection of inspiring quotes. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away", 
            link="https://kwotes.fr",
            button_text_1=["co-founder"],
            button_text_2=["mobile app"],
            
        ),  
        project_container(
            logo_src="/images/la_zebrelle.png", 
            title="la zébrelle", 
            description="The Savannah is an educational platform that promotes awareness, celebrates the diversity of neurodiversity, fostering inclusion and understanding for all", 
            link="https://lazebrelle.fr", 
            button_text_1=["founder"],
            button_text_2=["educational platform"],
        
        ),  
        project_container(
            logo_src="/images/africa_vivre.png", 
            title="africa vivre", 
            description="Embrace Africa's rich cultural diversity and support local artisans. Discover unique, handcrafted products made with passion and tradition", 
            link="https://www.africavivre.com",
            button_text_1=["associate"],
            button_text_2=["marketplace"], 
            
        ),
        width="100%",
        direction="column",
        align="center",
        justify="center", 
   ),          