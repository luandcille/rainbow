# ------------------------------------
# ℹ️ COMPONENT: CUSTOM BUTTONS
# ------------------------------------
# This file defines two reusable link-wrapped buttons:
# - primary_button: styled with bold text and icon
# - secondary_button: minimal outline style
# Both buttons support custom text and external links.


# --- 📦 Imports ---
import reflex as rx


# --- 🔘 Primary Button ---
def primary_button(
    button_text: list[str] = ["Button 1"],
    link: str = "#",
) -> rx.Component:
    return rx.link(
        rx.button(
            button_text,
            rx.icon(
                "arrow-up-right",
                size=20,
                color="black",
                margin_left="-6px",
                class_name=(
                    "transition-transform duration-200 ease-in-out "
                    "group-hover:translate-x-1 group-hover:-translate-y-1"
                ),
            ),
            color="black",
            font_family="Didact Gothic",
            font_weight="bold",
            background_color="white",
            radius="full",
            border="1px solid #000000",
            cursor="pointer",
            _hover={"opacity": 0.9},
            padding_left="15px",
            padding_right="10px",
        ),
        href=link,
        is_external=True,
        class_name="group",
    )


# --- ⚪ Secondary Button ---
def secondary_button(
    button_text: list[str] = ["Button 1"],
    link: str = "#",
) -> rx.Component:
    return rx.link(
        rx.button(
            button_text,
            font_family="Didact Gothic",
            size="3",
            color="black",
            weight="regular",
            background_color="white",
            radius="full",
            border="1px solid #000000",
            cursor="pointer",
            _hover={"opacity": 0.7},
            padding_left="20px",
            padding_right="20px",
        ),
        href=link,
        is_external=True,
    )
