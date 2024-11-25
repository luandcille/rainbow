"""Welcome to Lucille's journey!"""

import reflex as rx
from rxconfig import config

global_style = {
    "a": {
        "text_decoration": "none",
        "color": "inherit",
    },
    "a:hover": {
        "text_decoration": "none",
        "color": "inherit",
    },
}

def index() -> rx.Component:
    return rx.container(
        header(),
        body_content(),
        button_with_icon_after_text(),
        footer(),
   ),

def header():
    return rx.flex(
        rx.color_mode.button(position="top-right"),  # Light/Dark Mode
        rx.image(src="images/hello_lu.png", width="150px", height="150px"),
        rx.heading("HELLO, I AM LUCILLE", size="2", padding_bottom="5px", padding_top="10px"),
        rx.text("A Creative and Visionary", size="6", text_align="center", font_weight="bold", padding_bottom="-5px"),
        rx.text("Product Owner", size="6", text_align="center", margin_top="-4px", font_weight="bold", padding_bottom="15px"),
        rx.box(
            rx.link(
                rx.button(
                    "HIRE ME",
                    color="black",
                    background_color="white",
                    border="1px solid #000000",
                    border_radius="20px",
                    padding="10px 20px",
                    cursor="pointer",
                    _hover={"opacity": 0.8},
                ),
                href="https://www.linkedin.com/in/lucillevigne/",
            ),
            padding_bottom="50px",
        ),
        # Smooth scroll link
        rx.link(
            rx.icon(
                "circle-chevron-down",
                stroke_width=1.5,
                cursor="pointer",
                _hover=rx.color_mode_cond(
                    light={"color": "#333333", "opacity": 0.9},  # Light mode styles
                    dark={"color": "#FFFFFF", "opacity": 0.7},   # Dark mode styles
               ),
            ),
            href="#body_section",  # Ensure this targets the body section
            text_decoration="none",
            scroll=True,  # Reflex's smooth scrolling
            color="inherit",
            padding_bottom="100px",
            style={
                "display": "inline-block",  # Constrain the link to the icon's size
                "width": "fit-content",
                "height": "fit-content",
            },
            _hover={
                "color": "transparent",
                "text_decoration": "none",
            },
            # Add additional classes to remove default link styling
            class_name="no-hover-effect",
    
        ),
        width="100%",
        direction="column",
        align="center",
        justify="center",
        padding_top="200px",
    )

def body_content():
    return rx.flex(
        rx.box(  # Added a box wrapper with the id
            id="body_section",
            padding_top="120px"
        ),
        rx.container(
            rx.image(src="images/kwotes.png", width="80px", height="80px"), 
            rx.link(
                rx.flex(
                    rx.heading("kwotes app", size="8"),    
                    rx.icon("arrow-up-right", size=40),
                    _hover=rx.color_mode_cond(light={"opacity": 0.9, "color": "#333333"}, dark={"opacity": 0.7, "color": "#FFFFFF"},),),
                
                href="https://kwotes.fr/", 
                text_decoration="none",
                color="inherit",
            ),
            
            rx.flex( 
                rx.button(
                    "co-founder", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", 
                    size="1", 
                    padding_left="10px", 
                    padding_right="10px",
                ),

                rx.button(
                    "mobile app", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", size="1", 
                    padding_left="10px",  
                    padding_right="10px",
                ),
                
                # Style rx.flex
                spacing="2",
                padding_top="10px",
                padding_bottom="10px",
            ),
        
            rx.text("Kwotes offers a vast collection of inspiring quotes from diverse sources. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away"),

            # Style center the section
            width="45%",
        ),    
        rx.container(
            # La Zébrelle
            rx.image(src="images/la_zebrelle.png", width="80px", height="80px"), 
            rx.link(
                rx.flex(
                    rx.heading("la zébrelle", size="8"),    
                    rx.icon("arrow-up-right", size=40),
                    _hover=rx.color_mode_cond(light={"opacity": 0.9, "color": "#333333"}, dark={"opacity": 0.7, "color": "#FFFFFF"},),),
                
                href="https://lazebrelle.fr/", 
                text_decoration="none", 
                color="inherit",
            ),

            rx.flex( 
                rx.button(
                    "founder", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", 
                    size="1", 
                    padding_left="10px", 
                    padding_right="10px",
                ),

                rx.button(
                    "educational platform", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", size="1", 
                    padding_left="10px",  
                    padding_right="10px",
                ),
                
                # Style rx.flex
                spacing="2",
                padding_top="10px",
                padding_bottom="10px",
            ),
        
            rx.text("The Savannah is an educational platform that promotes awareness and celebrates the diversity of neurodiversity, fostering inclusion and understanding for all"),

            # Style center the section
            width="45%",
        ),
        rx.container(
            # Africa vivre 
            rx.image(src="images/africa_vivre.png", width="80px", height="80px"), 
            rx.link(
                rx.flex(
                    rx.heading("africa vivre", size="8"),    
                    rx.icon("arrow-up-right", size=40),
                    _hover=rx.color_mode_cond(light={"opacity": 0.9, "color": "#333333"}, dark={"opacity": 0.7, "color": "#FFFFFF"},),),
                
                href="https://www.africavivre.com/", 
                text_decoration="none", 
                color="inherit",
            ),
            rx.flex( 
                rx.button(
                    "co-founder", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", 
                    size="1", 
                    padding_left="10px", 
                    padding_right="10px",
                ),

                rx.button(
                    "marketplace", 
                    color="black", 
                    background_color="white", 
                    border="1px solid #000000",
                    padding="10px 20px", 
                    radius="full", size="1", 
                    padding_left="10px",  
                    padding_right="10px",
                ),
                
                # Style rx.flex
                spacing="2",
                padding_top="10px",
                padding_bottom="10px",
            ),
        
            rx.text("Embrace Africa's rich cultural diversity and support local artisans. Discover unique, handcrafted products made with passion and tradition"),

            # Style center the section 
            width="45%",
        ),
        # Style rx.container
        width="100%",
        direction="column",
        align="center",
        justify="center",
        padding_top="120px",
    ),
    
def button_with_icon_after_text():
    return rx.flex(
        rx.container( 
            rx.heading("Connect", size="7"),
            rx.flex(
                rx.link(
                    rx.button(
                        "linkedin", 
                        rx.icon("arrow-up-right", size=20 ,color="black", margin_left="-6px"),
                        color="black", 
                        background_color="white", 
                        border="1px solid #000000",
                        radius="full", 
                        size="2", 
                        padding_left="15px", 
                        padding_right="10px",
                        cursor="pointer",
                        _hover={"opacity": 0.8},
                    ),
                    href="https://www.linkedin.com/in/lucillevigne/"
                ),

                rx.link(
                    rx.button(
                        "cv.read", 
                        rx.icon("arrow-up-right", size=20 ,color="black", margin_left="-6px"),
                        color="black", 
                        background_color="white", 
                        border="1px solid #000000",
                        radius="full", 
                        size="2", 
                        padding_left="15px", 
                        padding_right="10px",
                        cursor="pointer",
                        _hover={"opacity": 0.8},
                        ),
                    href="https://read.cv/lucillevigne"
                ),
                
                rx.link(
                    rx.button(
                        "behance", 
                        rx.icon("arrow-up-right", size=20 ,color="black", margin_left="-6px"),
                        color="black", 
                        background_color="white", 
                        border="1px solid #000000",
                        radius="full", 
                        size="2", 
                        padding_left="15px", 
                        padding_right="10px",
                        cursor="pointer",
                        _hover={"opacity": 0.8},
                    ),
                href="https://www.behance.net/sonolucilla"
                ),
            # Style the buttons layout
            spacing="2",
            padding_top="10px",

            ), 

        # Center the entire section
        width="45%",

        ),
        # Center the entire section
        width="100%",
        direction="column",
        align_items="center",
        justify_content="center",
        padding_top="30px", 
    ), 

def footer():
    return rx.flex(
        rx.image(src="images/lucille_logo.png", width="50px", height="50px"),
        rx.text("Made by Lucille Vigné", size="2",padding_top="5px", letter_spacing="0.2px"),
        rx.text("Built with 🌈 and Reflex", size="2", padding_top="1px"),
        
        # Center the entire section
        spacing="-1",
        width="100%",
        direction="column",
        align="center",
        justify="center",
        padding_top="80px",
        padding_bottom="30px",
    ),

app = rx.App(style=global_style)
app.add_page(index)