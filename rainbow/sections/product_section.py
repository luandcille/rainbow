# ------------------------------------
# ℹ️ SECTION: PRODUCT PROJECTS
# ------------------------------------
# This file defines the content layout for the Product section.
# It pulls project data from a static data file and renders cards via `project_container`.


# --- 📦 Imports ---
import reflex as rx

from rainbow.components.portfolio.project_cards import project_container
from rainbow.data.product_card import product_projects, product_section_title


# --- 🛍️ Product Section Content ---
def product_section_content() -> rx.Component:
    return rx.el.div(
        rx.el.p(
            product_section_title,
            class_name="text-base md:text-lg text-left text-black-600 mb-12 max-w-2xl mx-auto",
        ),
        rx.el.div(
            rx.foreach(
                product_projects,
                lambda project: project_container(
                    logo_src=project["image_url"],
                    title=project["title"],
                    description=project["description"],
                    link=project["link"].to(str),
                    tags=project["tags"].to(list[str]),
                    date_range=project["date_range"],
                ),
            ),
            class_name="flex flex-col items-start space-y-8 max-w-md",
        ),
        class_name="flex flex-col items-center w-full",
    )
