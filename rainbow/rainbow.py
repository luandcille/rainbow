import reflex as rx
from rxconfig import config

from rainbow.sections.header import header
from rainbow.sections.body import body
from rainbow.sections.footer import footer
from rainbow.components.badge import badge
from rainbow.components.meta import meta_tags

app = rx.App(
    stylesheets = 
        ["fashion/main.css", 
         "https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap"
        ], 
)

@rx.page(
    title="Lucille Vigné · Beneath the Rainbow Sky",
    description="A creative and visionary space where ideas shine as brightly as rainbows, inspiring imagination and limitless possibilities.",
    image="images/lucille_vigne_rainbow.png",
    meta=meta_tags,
)
def index() -> rx.Component:
    return rx.container(
        header(),
        body(),
        footer(),
        badge(),
        class_name="rainbow-border",
        style={
            "backgroundColor": rx.color_mode_cond(
                light="#FDFCFC",  # Light mode background color
                dark="#1A1A1A",   # Dark mode background color
            )
        },
),
app.add_page(index)