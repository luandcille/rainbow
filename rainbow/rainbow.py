import reflex as rx
from rxconfig import config

from rainbow.sections.header import header
from rainbow.sections.body import body
from rainbow.sections.footer import footer
from rainbow.components.badge import badge


app = rx.App(
    stylesheets = 
        ["styles/style.css", 
         "https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap"
        ], 
)

def index() -> rx.Component:
    return rx.container(
        header(),
        body(),
        footer(),
        badge(),
        # class_name="flex flex-col w-full max-w-[94.5rem] justify-center items-center mx-auto px-4 lg:px-5 relative overflow-hidden",
   ),
app.add_page(index)