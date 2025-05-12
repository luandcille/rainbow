# ------------------------------------
# ℹ️ COMPONENT: PORTFOLIO CARDS
# ------------------------------------
# This file defines reusable card components used in the portfolio section.
# Each function returns a stylized card for Product, Dev, or Design sections,
# with image, title, description, tags, and interactivity like links or modals.


# --- 📦 Imports ---
import reflex as rx

# 🧠 App State
from rainbow.state.portfolio_state import DesignDevProject
from rainbow.state.modal_state import ModalState

# --- 📅 Product Card (for static products or links) ---
import reflex as rx


def project_container(
    logo_src: str = "/images/default.png",
    title: str = "Default Title",
    description: str = "Default description text goes here.",
    date_range: str = "",
    link: str = "#",
    tags: list[str] = [],
) -> rx.Component:
    return rx.flex(
        rx.container(
            # Image (logo)
            rx.image(
                src=logo_src,
                width="65px",
                height="65px",
                margin_bottom="10px"
            ),

            # Title + icon
            rx.link(
                rx.flex(
                    rx.heading(
                        title,
                        size="8",
                        text_align="center",
                        margin_bottom="2px",
                        font_family="Didact Gothic",
                        weight="regular"
                    ),
                    rx.icon(
                        "arrow-up-right",
                        stroke_width=1.4,
                        size=30,
                        margin_bottom="2px",
                        class_name="transition-transform duration-200 ease-in-out group-hover:translate-x-1 group-hover:-translate-y-1"
                    ),
                    _hover=rx.color_mode_cond(
                        light={"opacity": 0.9, "color": "#333333"},
                        dark={"opacity": 0.7, "color": "#FFFFFF"},
                    ),
                ),
                href=link,
                is_external=True,
                text_decoration="none",
                color="inherit",
                class_name="group",
            ),

            # Date Range 
            rx.el.p(date_range, class_name="text-xs mb-3", color=rx.color_mode_cond(light="gray.500",dark="white"),
            ),


            # Tags
            rx.flex(
                rx.foreach(
                    tags,
                    lambda tag: rx.button(
                        tag,
                        font_family="Didact Gothic",
                        font_weight="600",
                        radius="full", 
                        color="black",
                        background_color="white",
                        border="1px solid #000000",
                        size="1",
                        padding_left="10px",
                        padding_right="10px",
                        margin_top="2px",
                        margin_bottom="6px",
                    ),
                ),
                spacing="1",
            ),

            # Description
            rx.text(
                description,
                size="4",
                font_family="Didact Gothic",
                weight="regular",
                margin_top="3px"
            ),

            width="400px",
        ),
        padding_top="10px",
    )


# --- 🚀 Dev Card (for developer projects with images and tags) ---
def dev_card(project: DesignDevProject) -> rx.Component:
    return rx.flex(
        rx.el.div(
            # Entire card block (including image + body) gets the border, radius, shadow
            rx.el.div(
                rx.el.img(
                    src=project["image_url"],
                    alt=f"{project['title']} preview",
                    class_name="w-full h-52 object-cover transition-transform duration-300 ease-in-out group-hover:scale-105 rounded-t-lg",
                ),
            ),
            rx.el.div(
                rx.link(
                    rx.flex(
                        rx.heading(
                            project["title"],
                            size="8",
                            text_align="center",
                            margin_bottom="2px",
                            font_family="Didact Gothic",
                            weight="regular",
                            color="black",
                        ),
                        rx.icon(
                            "arrow-up-right",
                            stroke_width=1.4,
                            size=30,
                            margin_bottom="2px",
                            color="black",
                            class_name="transition-transform duration-200 ease-in-out group-hover:translate-x-1 group-hover:-translate-y-1",
                        ),
                        _hover=rx.color_mode_cond(
                            light={"opacity": 0.9, "color": "#333333"},
                            dark={"opacity": 0.7, "color": "#FFFFFF"},
                        ),
                    ),
                    href=project["link"],
                    is_external=True,
                    text_decoration="none",
                    color=rx.color_mode_cond(light="#000000", dark="#FFFFFF"),
                    _hover=rx.color_mode_cond(light={"opacity": 0.9, "color": "#333333"}, dark={"opacity": 0.7, "color": "#FFFFFF"}),
                    class_name="group",
                ),
                rx.el.p(project["date_range"], class_name="text-xs text-gray-500 mb-3"),
                
                rx.flex(
                    rx.foreach(
                        project["tags"].to(list[str]),
                        lambda tag: rx.button(
                            tag,
                            font_family="Didact Gothic",
                            font_weight="600",
                            radius="full",
                            color="black",
                            background_color="white",
                            border="1px solid #000000",
                            size="1",
                            padding_left="10px",
                            padding_right="10px",
                            margin_top="2px",
                            margin_bottom="10px",
                        ),
                    ),
                    spacing="1",
                ),
                rx.el.p(
                    project["description"],
                    class_name="text-[1.05rem] text-black mb-4 text-left",
                ),
                class_name="px-4 pb-4 pt-3",
            ),
            class_name=(
                "group flex flex-col w-full max-w-sm bg-white rounded-lg border border-gray-200 "
                "overflow-hidden hover:shadow-lg dark:hover:shadow-[0_4px_6px_rgba(0,0,0,0.1),_0_4px_14px_rgba(255,255,255,0.1)] "
                "transition-shadow duration-200"
            ),
        ),
        padding_top="26px",
        padding_bottom="50px",
    )


# --- 🌟 Design Card (triggers modal on click) ---
def design_card(project: DesignDevProject) -> rx.Component:
    return rx.flex(
        rx.el.div(
            # --- Image wrapper with shadow, border, and rounded corners ---
            rx.box(
                rx.el.img(
                    src=project["image_url"],
                    alt=f"{project['title']} preview",
                    class_name=(
                        "w-full h-64 object-cover transition-transform duration-300 "
                        "ease-in-out group-hover:scale-105"
                    ),
                ),
                on_click=ModalState.open_modal(project["id"]),
                cursor="pointer",
                class_name=(
                    "w-full h-64 rounded-lg border border-gray-200 overflow-hidden "
                    "hover:shadow-lg dark:hover:shadow-[0_4px_6px_rgba(0,0,0,0.1),_0_4px_14px_rgba(255,255,255,0.1)] "
                    "transition-shadow duration-200"
                ),
            ),

            # --- Title and Tags ---
            rx.el.div(
                rx.flex(
                    rx.box(
                        rx.flex(
                            rx.heading(
                                project["title"],
                                size="7",
                                text_align="left",
                                font_family="Didact Gothic",
                                weight="regular",
                                margin_bottom="0px",
                            ),
                            rx.icon(
                                tag="arrow_right",
                                size=24,
                                class_name="ml-2 mt-1 transition-transform duration-200 ease-in-out group-hover:translate-x-1",
                            ),
                            class_name="flex items-center space-x-2",
                        ),
                        on_click=ModalState.open_modal(project["id"]),
                        cursor="pointer",
                        _hover={"opacity": "0.9"},
                        class_name="group",
                    ),
                    rx.flex(
                        rx.foreach(
                            project["tags"].to(list[str]),
                            lambda tag: rx.button(
                                tag,
                                font_family="Didact Gothic",
                                font_weight="600",
                                radius="full",
                                color="black",
                                background_color="white",
                                border="1px solid #000000",
                                size="1",
                                padding_left="10px",
                                padding_right="10px",
                                margin_top="5px",
                                margin_bottom="5px",
                            ),
                        ),
                        spacing="1",
                        margin_left="auto",
                        class_name="flex items-center",
                    ),
                    class_name="flex w-full items-center",
                ),
                class_name="flex flex-col items-start justify-start mt-1",
            ),

            class_name="group flex flex-col w-full max-w-sm",
        ),
        padding_top="26px",
        padding_bottom="50px",
    )


