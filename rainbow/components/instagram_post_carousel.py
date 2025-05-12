# ------------------------------------
# ℹ️ COMPONENT: INSTAGRAM POST CAROUSEL
# ------------------------------------
# This file defines an Instagram-like carousel with image navigation,
# bullets overlay, a like button with count, and a custom caption.
# It uses `ModalState` to manage image index and like count per post.


# --- 📦 Imports ---
import reflex as rx
from typing import List

# 📂 State
from rainbow.state.modal_state import ModalState


# --- 📸 Instagram Post Carousel ---
def instagram_post_carousel(
    image_sources: List[str],
    alt_text: str,
    caption_text: str = "Made with love ❤️",
    post_width: str = "300px",
    image_height: str = "300px",
    post_id: str = "carousel",
) -> rx.Component:
    images_var = rx.Var.create(image_sources)

    return rx.el.div(
        # 🖼️ Image section with arrows and bullets
        rx.el.div(
            # ⬅️ Left arrow
            rx.el.button(
                rx.icon(tag="arrow-left", class_name="w-4 h-4"),
                on_click=lambda: ModalState.prev_instagram_image(image_sources),
                class_name=(
                    "absolute -left-10 top-1/2 transform -translate-y-1/2 "
                    "bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 "
                    "transition-opacity duration-200 z-10"
                ),
                disabled=len(image_sources) <= 1,
            ),
            # 🖼️ Main image + bullets overlay
            rx.el.div(
                rx.foreach(
                    images_var,
                    lambda img, index: rx.cond(
                        index == ModalState.instagram_image_index,
                        rx.el.div(
                            rx.image(
                                src=img,
                                alt=alt_text,
                                class_name=f"w-full h-[{image_height}] object-cover rounded-t-lg",
                            ),
                            rx.el.div(
                                rx.foreach(
                                    list(range(len(image_sources))),
                                    lambda bullet_index: rx.el.span(
                                        class_name=rx.cond(
                                            bullet_index == ModalState.instagram_image_index,
                                            "block w-1.5 h-1.5 bg-white rounded-full mx-0.5",
                                            "block w-1.5 h-1.5 bg-gray-300 rounded-full mx-0.5",
                                        )
                                    ),
                                ),
                                class_name="absolute bottom-2 left-1/2 transform -translate-x-1/2 flex items-center",
                            ),
                            class_name="relative",
                        ),
                        rx.fragment(),
                    ),
                ),
                class_name="rounded-t-lg overflow-hidden",
            ),
            # ➡️ Right arrow
            rx.el.button(
                rx.icon(tag="arrow-right", class_name="w-4 h-4"),
                on_click=lambda: ModalState.next_instagram_image(image_sources),
                class_name=(
                    "absolute -right-10 top-1/2 transform -translate-y-1/2 "
                    "bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 "
                    "transition-opacity duration-200 z-10"
                ),
                disabled=len(image_sources) <= 1,
            ),
            class_name="relative w-full group",
        ),
        # ❤️ Like count + caption
        rx.el.div(
            rx.el.div(
                rx.el.button(
                    rx.icon(
                        tag="heart",
                        class_name=rx.cond(
                            ModalState.love_counts.get(post_id, 0) >= 1,
                            "w-6 h-6 stroke-red-500 fill-red-500",
                            "w-6 h-6 stroke-gray-800 fill-none",
                        ),
                    ),
                    on_click=lambda: ModalState.increment_love_count(post_id),
                    class_name=(
                        "hover:bg-gray-100 rounded-full p-1 "
                        "transition transform active:scale-125 duration-200"
                    ),
                ),
                rx.el.p(
                    f"{ModalState.love_counts.get(post_id, 0)} likes",
                    class_name="font-semibold text-sm text-gray-900 ml-2",
                ),
                class_name="flex items-center justify-start mb-2",
            ),
            rx.el.p(
                caption_text,
                class_name="font-semibold text-sm text-gray-900 ml-2 mb-3 mt-2",
            ),
            class_name="p-3",
        ),
        class_name="bg-white shadow-md rounded-lg mb-10 mx-auto",
        style={"width": post_width},
    )
