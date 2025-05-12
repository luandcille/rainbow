# ------------------------------------
# ℹ️ COMPONENT: HINT (Hover Tooltip)
# ------------------------------------

# This file defines a reusable tooltip-style component using Reflex HoverCard.
# It displays a small text hint when hovering over any given component.

# --- 📦 Imports ---
import reflex as rx


# --- 💡 Hint Component ---
def hint(
    text: str,
    content: rx.Component,
    side: str = "top",
    align: str = "center",
    active: bool = False,
    class_name: str = "",
    **props
) -> rx.Component:
    return rx.hover_card.root(
        rx.hover_card.trigger(content, height="fit-content"),
        rx.hover_card.content(
            rx.text(text),
            side=side,
            align=align,
            class_name="flex justify-center items-center bg-slate-11 px-1.5 py-0.5 rounded-lg font-small text-white-1",
        ),
        class_name=class_name,
        default_open=active,
        open_delay=80,
        close_delay=80,
        **props,
    )
