# ------------------------------------
# 🌈 MAIN APP ENTRYPOINT
# ------------------------------------
# This file defines the Reflex app configuration and homepage layout.
# It uses components like header, footer, badge, and the portfolio section.


# --- 📦 Imports ---
import reflex as rx

from rainbow.components.header import header
from rainbow.components.footer import footer
from rainbow.components.badge import badge
from rainbow.components.meta import meta_tags
from rainbow.components.portfolio.portfolio import portfolio_section


# --- 🔄 App State ---
class State(rx.State):
    """The app state."""
    ...


# --- 🏠 Page: Home ---
@rx.page(
    title="Lucille Vigné · Beneath the Rainbow Sky",
    description="A creative and visionary space where ideas shine as brightly as rainbows, inspiring imagination and limitless possibilities.",
    image="images/lucille_vigne_rainbow.png",
    meta=meta_tags,
)
def index() -> rx.Component:
    return rx.container(
        header(),
        portfolio_section(),
        footer(),
        rx.el.style( 
            """
            a[href="https://reflex.dev"] {
                display: none !important;
            }
            """
        ),
        badge(),
        class_name="rainbow-border font-didact",
        style={
            "backgroundColor": rx.color_mode_cond(
                light="#FDFCFC",
                dark="#1A1A1A",
            )
        },
    )


# --- 🚀 App Setup ---
app = rx.App(
    stylesheets=[
        "styles/main.css",
        "https://fonts.googleapis.com/css2?family=Didact+Gothic&display=swap",
    ],
)
app.add_page(index)


