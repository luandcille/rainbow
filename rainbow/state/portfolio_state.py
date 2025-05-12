# ------------------------------------
# 🧠 STATE: PORTFOLIO STATE
# ------------------------------------
# This file defines the PortfolioState class for managing active section
# and providing access to Dev and Design project data from `data/`.


# --- 📦 Imports ---
import reflex as rx
from typing import TypedDict, List

from rainbow.data.dev_card import dev_projects 
from rainbow.data.design_card import design_projects


# --- 📊 Data Types ---
class DesignDevProject(TypedDict):
    id: str
    title: str
    description: str
    date_range: str
    image_url: str
    tags: List[str]
    link: str


# --- 🧩 Portfolio State ---
class PortfolioState(rx.State):
    """The application state."""

    current_section: str = "Product"
    dev_projects: List[DesignDevProject] = dev_projects
    design_projects: List[DesignDevProject] = design_projects

    @rx.event
    def set_section(self, section: str):
        """Sets the current section to display."""
        self.current_section = section




# import reflex as rx
# from typing import TypedDict, List
# from rainbow.data.dev_card import dev_projects 
# from rainbow.data.design_card import design_projects


# class DesignDevProject(TypedDict):
#     id: str
#     title: str
#     description: str
#     date_range: str
#     image_url: str
#     tags: List[str]
#     link: str


# class PortfolioState(rx.State):
#     """The application state."""

#     current_section: str = "Product"
#     dev_projects: List[DesignDevProject] = dev_projects
#     design_projects: List[DesignDevProject] = design_projects

#     @rx.event
#     def set_section(self, section: str):
#         """Sets the current section to display."""
#         self.current_section = section