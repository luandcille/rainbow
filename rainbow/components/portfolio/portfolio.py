# ------------------------------------
# ℹ️ COMPONENT: PORTFOLIO SECTION
# ------------------------------------
# Defines the interactive Portfolio section with 3 tabs: Product, Code, Design.
# Dynamically switches content using `PortfolioState` and renders the associated
# section layout depending on user interaction. Also includes modal pop-ups via `pop_up()`.


# --- 📦 Imports ---
import reflex as rx

# 🧠 App State
from rainbow.state.portfolio_state import PortfolioState
from rainbow.state.modal_state import ModalState

# 📂 Sections (content sources)
from rainbow.sections.product_section import product_section_content
from rainbow.sections.dev_section import dev_section_content
from rainbow.sections.design_section import design_section_content

# 🧩 UI Components
from rainbow.components.pop_up.pop_up import pop_up


# ------------------------------------
# 🔘 Section Switch Button
# ------------------------------------
def section_button(text: str, section_name: str) -> rx.Component:
    """A minimalist button for section selection with active state emphasis."""
    return rx.el.span(
        text,
        on_click=lambda: PortfolioState.set_section(section_name),
        class_name=rx.cond(
            PortfolioState.current_section == section_name,
            # Active tab style
            "text-lg font-bold text-black-600 cursor-pointer transition-all duration-200 px-2",
            # Inactive tab style
            "text-base text-gray-600 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100 px-2",
        ),
    )


# ------------------------------------
# 🧱 Main Portfolio Section
# ------------------------------------
def portfolio_section() -> rx.Component:
    """The portfolio section with minimalist tabs and centered project blocks."""
    return rx.el.div(
        rx.box(  # Anchor offset to scroll correctly
            id="body",
            padding_top="100px",
        ),

        rx.el.div(
            # Tabs + Modals
            rx.el.div(
                section_button("Product", "Product"),
                section_button("Code", "Code"),
                section_button("Design", "Design"),
                pop_up(),
                class_name="flex justify-center space-x-4 sm:space-x-8 mb-12 items-baseline",
            ),

            # Dynamic content block
            rx.el.div(
                rx.match(
                    PortfolioState.current_section,
                    ("Product", product_section_content()),
                    ("Code", dev_section_content()),
                    ("Design", design_section_content()),
                    rx.el.p("Select a section."),  # Fallback
                ),
                class_name="w-full flex justify-center",
            ),

            class_name="w-full flex flex-col items-center",
        ),

        id="portfolio-section",
        class_name="py-16 sm:py-24 px-4 sm:px-8 md:px-16",
    )



# import reflex as rx
# from rainbow.state.portfolio_state import PortfolioState
# from rainbow.sections.product_section import product_section_content
# from rainbow.sections.dev_section import dev_section_content
# from rainbow.sections.design_section import design_section_content
# from rainbow.components.pop_up.pop_up import pop_up
# from rainbow.state.modal_state import ModalState



# def section_button(
#     text: str, section_name: str
# ) -> rx.Component:
#     """A minimalist button for section selection with active state emphasis."""
#     return rx.el.span(
#         text,
#         on_click=lambda: PortfolioState.set_section(
#             section_name
#         ),
#         class_name=rx.cond(
#             PortfolioState.current_section == section_name,
#             "text-lg font-bold text-black-600 cursor-pointer transition-all duration-200 px-2",
#             "text-base text-gray-600 dark:text-gray-400 hover:text-gray-700 dark:hover:text-gray-200 cursor-pointer transition-all duration-200 opacity-60 hover:opacity-100 px-2",
#         ),
#     )


# def portfolio_section() -> rx.Component:
#     """The portfolio section with minimalist tabs and centered project blocks."""
#     return rx.el.div(
#         rx.box(  # Function of the anchor
#             id="body",
#             padding_top="100px",
#         ),
#         rx.el.div(
#             rx.el.div(
#                 section_button("Product", "Product"),
#                 section_button("Code", "Code"),
#                 section_button("Design", "Design"),
#                 pop_up(),
                
#                 class_name="flex justify-center space-x-4 sm:space-x-8 mb-12 items-baseline",
#             ),
#             rx.el.div(
#                 rx.match(
#                     PortfolioState.current_section,
#                     ("Product", product_section_content()),
#                     ("Code", dev_section_content()),
#                     ("Design", design_section_content()),
#                     rx.el.p("Select a section."),
#                 ),
#                 class_name="w-full flex justify-center",
#             ),
#             class_name="w-full flex flex-col items-center",
#         ),
#         id="portfolio-section",
#         class_name="py-16 sm:py-24 px-4 sm:px-8 md:px-16",
#     )