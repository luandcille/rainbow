# ------------------------------------
# ℹ️ COMPONENT: CAROUSEL
# ------------------------------------
# This file defines a reusable image carousel with left/right arrows,
# bullet navigation inside the image, and an optional caption below.
# It relies on ModalState to track current image index.


# --- 📦 Imports ---
import reflex as rx
from typing import List, Optional

# 📂 State
from rainbow.state.modal_state import ModalState


# --- 🖼️ Carousel Component ---
def carousel_component(
    images: List[str],
    post_width: str = "350px",
    image_height: str = "300px",
    caption: Optional[str] = None,
) -> rx.Component:
    """Reusable carousel with bullets inside the image and optional caption underneath."""
    return rx.el.div(
        rx.el.div(
            # 🖼️ Image + arrows + bullets overlay
            rx.el.div(
                # ⬅️ Left Arrow
                rx.el.button(
                    rx.icon(tag="arrow-left", class_name="w-4 h-4"),
                    on_click=lambda: ModalState.prev_image(images),
                    class_name=(
                        "absolute -left-10 top-1/2 transform -translate-y-1/2 "
                        "bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 "
                        "transition-opacity duration-200 z-10"
                    ),
                    disabled=len(images) <= 1,
                ),
                # 🖼️ Image
                rx.el.div(
                    rx.foreach(
                        images,
                        lambda img, index: rx.cond(
                            index == ModalState.current_image_index,
                            rx.image(
                                src=img,
                                alt="Carousel Image",
                                class_name=f"rounded-lg shadow-lg object-cover w-full h-[{image_height}]",
                            ),
                            rx.fragment(),
                        ),
                    ),
                    class_name="w-full flex items-center justify-center shadow-lg rounded-lg overflow-hidden relative",
                    style={"width": post_width},
                ),
                # ➡️ Right Arrow
                rx.el.button(
                    rx.icon(tag="arrow-right", class_name="w-4 h-4"),
                    on_click=lambda: ModalState.next_image(images),
                    class_name=(
                        "absolute -right-10 top-1/2 transform -translate-y-1/2 "
                        "bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 "
                        "transition-opacity duration-200 z-10"
                    ),
                    disabled=len(images) <= 1,
                ),
                # 🔘 Bullets (inside image)
                rx.el.div(
                    rx.foreach(
                        list(range(len(images))),
                        lambda index: rx.el.span(
                            class_name=rx.cond(
                                index == ModalState.current_image_index,
                                "block w-1.5 h-1.5 bg-white rounded-full mx-1 cursor-pointer",
                                "block w-1.5 h-1.5 bg-gray-300 rounded-full mx-1 cursor-pointer hover:bg-gray-400",
                            )
                        ),
                    ),
                    class_name=(
                        "absolute bottom-2 left-1/2 transform -translate-x-1/2 "
                        "flex justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-200"
                    ),
                ),
                class_name="relative w-full group",
            ),
            # 📝 Optional caption
            rx.el.p(
                caption,
                class_name="text-sm text-gray-500 italic text-center mt-3",
            ) if caption else rx.fragment(),
            class_name="flex flex-col items-center",
        ),
        class_name="flex flex-col items-center",
    )





# # rainbow/components/carousel_component.py

# import reflex as rx
# from typing import List
# from rainbow.state.modal_state import ModalState

# def carousel_component(
#     images: List[str],
#     post_width: str = "350px",
#     image_height: str = "300px",
# ) -> rx.Component:
#     """Reusable carousel with hover-only arrows and bullets."""
#     return rx.el.div(
#         rx.el.div(  # Group container to control hover state
#             # ⬅️ Arrows + Image
#             rx.el.div(
#                 rx.el.button(
#                     rx.icon(tag="arrow-left", class_name="w-4 h-4"),
#                     on_click=lambda: ModalState.prev_image(images),
#                     class_name="absolute -left-10 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 transition-opacity duration-200 z-10",
#                     disabled=len(images) <= 1,
#                 ),
#                 rx.el.div(
#                     rx.foreach(
#                         images,
#                         lambda img, index: rx.cond(
#                             index == ModalState.current_image_index,
#                             rx.image(
#                                 src=img,
#                                 alt="Carousel Image",
#                                 class_name=f"rounded-lg shadow-lg object-cover w-full h-[{image_height}]",
#                             ),
#                             rx.fragment(),
#                         ),
#                     ),
#                     class_name=f"w-full flex items-center justify-center shadow-lg rounded-lg overflow-hidden",
#                     style={"width": post_width},
#                 ),
#                 rx.el.button(
#                     rx.icon(tag="arrow-right", class_name="w-4 h-4"),
#                     on_click=lambda: ModalState.next_image(images),
#                     class_name="absolute -right-10 top-1/2 transform -translate-y-1/2 bg-gray-800 text-white p-2 rounded-full opacity-0 group-hover:opacity-80 transition-opacity duration-200 z-10",
#                     disabled=len(images) <= 1,
#                 ),
#                 class_name="relative w-full group",
#             ),
#             # ⬇️ Bullets
#             rx.el.div(
#                 rx.foreach(
#                     list(range(len(images))),
#                     lambda index: rx.el.span(
#                         class_name=rx.cond(
#                             index == ModalState.current_image_index,
#                             "block w-1.5 h-1.5 bg-gray-800 rounded-full mx-1 cursor-pointer",
#                             "block w-1.5 h-1.5 bg-gray-400 rounded-full mx-1 cursor-pointer hover:bg-gray-600",
#                         )
#                     ),
#                 ),
#                 class_name="flex justify-center mt-6 pb-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200",
#             ),
#             class_name="group",  # ✅ group for hover behavior
#         ),
#         class_name="flex flex-col items-center",
#     )


