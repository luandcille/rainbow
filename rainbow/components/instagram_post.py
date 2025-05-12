# ------------------------------------
# ℹ️ COMPONENT: INSTAGRAM POST
# ------------------------------------
# This file defines a reusable Instagram-style post card.
# It includes a single image, a like button with animated feedback,
# and a custom caption underneath.
# The number of likes is stored in `ModalState.love_counts`.


# --- 📦 Imports ---
import reflex as rx

# 📂 State
from rainbow.state.modal_state import ModalState


# --- 📸 Instagram Post Component ---
def instagram_post(
    image_src: str,
    alt_text: str,
    caption_text: str = "Made with love ❤️",
    post_width: str = "300px",
    image_height: str = "auto",
) -> rx.Component:
    """Reusable Instagram-style post component with like button and caption."""
    return rx.el.div(
        # 🖼️ Image
        rx.image(
            src=image_src,
            alt=alt_text,
            class_name=f"w-full h-[{image_height}] object-cover rounded-t-lg",
        ),
        # ❤️ Like button + caption
        rx.el.div(
            # Like + Count
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        tag="heart",
                        class_name=rx.cond(
                            ModalState.love_counts.get(image_src, 0) >= 1,
                            "w-6 h-6 stroke-red-500 fill-red-500",
                            "w-6 h-6 stroke-gray-800 fill-none",
                        ),
                    ),
                    on_click=lambda: ModalState.increment_love_count(image_src),
                    class_name=(
                        "hover:bg-gray-100 rounded-full p-1 "
                        "transition transform active:scale-125 duration-200"
                    ),
                ),
                rx.el.p(
                    f"{ModalState.love_counts.get(image_src, 0)} likes",
                    class_name="font-semibold text-sm text-gray-900 ml-2",
                ),
                class_name="flex items-center",
            ),
            # Caption
            rx.el.p(
                caption_text,
                class_name="font-semibold text-sm text-gray-900 ml-2 mb-3 mt-2",
            ),
            class_name="p-3",
        ),
        class_name="bg-white shadow-md rounded-lg mb-10 mx-auto",
        style={"width": post_width},
    )
