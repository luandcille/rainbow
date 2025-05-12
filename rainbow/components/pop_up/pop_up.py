# ------------------------------------
# ℹ️ COMPONENT: POP-UP WRAPPER
# ------------------------------------
# Serves as the central entry point for all individual pop-up designs.
# It conditionally renders pop-ups (e.g., design_1, design_2, design_3)
# based on the `active_modal_id` from `ModalState`.
# Each pop-up is defined in its own module for modularity and clarity.


# --- 📦 Imports ---
import reflex as rx

# ⬇️ Import all individual pop-up designs from the current module
from . import (
    pop_up_design_1,
    pop_up_design_2,
    pop_up_design_3,
)

# --- ⚙️ Main function ---
def pop_up() -> rx.Component:
    """Returns all defined pop-up designs to be rendered in the app."""
    return rx.fragment(
        pop_up_design_1(),
        pop_up_design_2(),
        pop_up_design_3(),
    )


# import reflex as rx
# from rainbow.components.pop_up.pop_up_design_1 import pop_up_design_1
# from rainbow.components.pop_up.pop_up_design_2 import pop_up_design_2
# from rainbow.components.pop_up.pop_up_design_3 import pop_up_design_3


# def pop_up() -> rx.Component:
#     return rx.fragment(
#         pop_up_design_1(),
#         pop_up_design_2(),
#         pop_up_design_3(), 
#     )

