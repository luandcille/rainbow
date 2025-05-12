# ------------------------------------
# ℹ️ SECTION: DESIGN PROJECTS
# ------------------------------------
# This file defines the content layout for the Design section.
# It pulls project data from PortfolioState and renders cards via `design_card`.


# --- 📦 Imports ---
import reflex as rx

from rainbow.state.portfolio_state import PortfolioState
from rainbow.components.portfolio.project_cards import design_card
from rainbow.data.design_card import design_section_title 


# --- 🎨 Design Section Content ---
def design_section_content() -> rx.Component:
    """Content for the Design section, text aligned left but block centered."""
    return rx.el.div(
        rx.el.p(
            design_section_title,
            class_name="text-base md:text-lg text-left text-black-600 mb-12 max-w-2xl mx-auto",
        ),
        rx.el.div(
            rx.foreach(
                PortfolioState.design_projects,
                design_card,
            ),
            class_name="flex flex-col items-start space-y-8 max-w-md",
        ),
        class_name="flex flex-col items-center w-full",
    )
