# ------------------------------------
# ℹ️ SECTION: DEV PROJECTS
# ------------------------------------
# This file defines the content layout for the Dev section.
# It pulls project data from PortfolioState and renders cards via `dev_card`.


# --- 📦 Imports ---
import reflex as rx

from rainbow.components.portfolio.project_cards import dev_card
from rainbow.state.portfolio_state import PortfolioState
from rainbow.data.dev_card import dev_section_title


# --- 💻 Dev Section Content ---
def dev_section_content() -> rx.Component:
    """Content for the Dev section, text aligned left but block centered."""
    return rx.el.div(
        rx.el.p(
            dev_section_title,
            class_name="text-base md:text-lg text-left text-black-600 mb-12 max-w-2xl mx-auto",
        ),
        rx.el.div(
            rx.foreach(
                PortfolioState.dev_projects,
                lambda project: dev_card(project),
            ),
            class_name="flex flex-col items-start space-y-8 max-w-md",
        ),
        class_name="flex flex-col items-center w-full",
    )
