import reflex as rx
from rxconfig import config

from rainbow.sections.header import header
from rainbow.sections.body import body
from rainbow.sections.footer import footer

app = rx.App(
    stylesheets = ["styles/style.css"], 
)

def index() -> rx.Component:
    return rx.container(
        header(),
        body(),
        footer(),
   ),
app.add_page(index)