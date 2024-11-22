import reflex as rx
from rxconfig import config
from rainbow.components.buttons import primary_button, secondary_button
from rainbow.components.projects import project

app = rx.App(stylesheets = ["/styles.css"])

def index() -> rx.Component:
    return rx.container(
        header(),
        body(),
        footer(),
   ),

def header() -> rx.Component:
    return rx.box(
        
app.add_page(index)