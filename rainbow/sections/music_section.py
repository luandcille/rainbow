# ------------------------------------
# ℹ️ SECTION: MUSIC PROJECTS
# ------------------------------------
# This file defines the content layout for the Design section.
# It pulls project data from PortfolioState and renders cards via `design_card`.


# --- 📦 Imports ---
import reflex as rx

from rainbow.state.portfolio_state import PortfolioState
from rainbow.components.portfolio.project_cards import music_card
from rainbow.data.music_card import music_section_title 


# --- 🎨 Design Section Content ---
def music_section_content() -> rx.Component:
    """Content for the Design section, text aligned left but block centered."""
    return rx.el.div(
        rx.el.p(
            music_section_title,
            class_name="text-base md:text-lg text-left text-black-600 mb-12 max-w-2xl mx-auto",
        ),
        rx.el.div(
            rx.foreach(
                PortfolioState.music_projects,
                music_card,
            ),
            class_name="flex flex-col items-start space-y-18 max-w-md",
        ),
        class_name="flex flex-col items-center w-full",
    )
