# ------------------------------------
# ℹ️ COMPONENT: POP-UP DESIGN 1
# ------------------------------------
# This file defines the first pop-up layout for the project "La Squadra Italiana".
# It fetches content from `POPUP_CONTENT["squadra"]` and builds a scrollable modal
# with a header, highlights, Instagram-style carousel, image gallery, and a quote.


# --- 📦 Imports ---
import reflex as rx

# 🧠 App State
from rainbow.state.modal_state import ModalState

# 📊 Data
from rainbow.data.pop_up_design_content import POPUP_CONTENT

# 🧩 UI Components
from rainbow.components.carousel import carousel_component
from rainbow.components.instagram_post_carousel import instagram_post_carousel
# from rainbow.components.instagram_post import instagram_post  # currently unused


# --- 🧩 Component ---
def pop_up_design_1() -> rx.Component:
    """Renders the Squadra pop-up modal if the active_modal_id is 'squadra'."""
    content = POPUP_CONTENT["squadra"]

    return rx.cond(
        ModalState.active_modal_id == "squadra",
        rx.el.div(
            rx.el.div(
                # Close button
                rx.el.button(
                    rx.icon(tag="x", class_name="w-5 h-5"),
                    on_click=ModalState.close_modal,
                    class_name=(
                        "absolute top-5 right-5 z-20 p-1.5 bg-gray-800 text-white "
                        "rounded-full hover:bg-gray-700 focus:outline-none focus:ring-2 "
                        "focus:ring-gray-500 focus:ring-offset-2 transition-colors duration-200"
                    ),
                ),
                rx.scroll_area(
                    rx.el.div(
                        # 📌 Header (Case study + Title + Hero image)
                        rx.el.div(
                            rx.el.p(
                                content["case_study"],
                                class_name="text-sm text-gray-500 text-center pt-16",
                            ),
                            # ✅ Date Range
                            rx.el.p(
                                content["date_range"],
                                class_name="text-sm text-gray-500 mb-3 text-center",
                            ),
                            rx.el.h2(
                                content["title"],
                                class_name="text-3xl font-bold text-gray-900 mb-8 text-center",
                            ),
                            rx.el.div(
                                rx.image(
                                    src=content["image1"],
                                    alt=content["image1_alt"],
                                    class_name="rounded-lg shadow-lg w-[450px] h-[200px] object-cover mx-auto",
                                ),
                                class_name="w-full mb-10",
                            ),
                            class_name="w-full",
                        ),

                        # 📖 Introduction
                        rx.el.div(
                            rx.el.h3(content["intro_title"], class_name="text-xl font-semibold text-gray-900 mb-3"),
                            rx.el.p(content["intro"], class_name="text-gray-700 leading-relaxed text-base mb-8"),
                            rx.el.div(
                                rx.image(
                                    src=content["image2"],
                                    alt=content["image2_alt"],
                                    class_name="rounded-lg shadow-lg w-full h-auto object-cover mx-auto",
                                ),
                                class_name="w-full mb-8",
                            ),
                            class_name="mb-10 w-9/12",
                        ),

                        # ⭐ Highlight 1
                        rx.el.div(
                            rx.el.h4(content["highlight1_subtitle"], class_name="text-xl font-semibold text-gray-900 mb-3"),
                            rx.el.p(content["highlight1_content"], class_name="text-gray-700 leading-relaxed text-base mb-10"),
                            class_name="w-9/12",
                        ),

                        # 📸 Instagram carousel
                        instagram_post_carousel(
                            image_sources=content["instagram_post_carousel_images"],
                            alt_text=content["instagram_post_carousel_alt"],
                            caption_text=content["instagram_post_carousel_caption"],
                            post_width="350px",
                            image_height="300px",
                            post_id="squadra_carousel",
                        ),

                        # ⭐ Highlight 2
                        rx.el.div(
                            rx.el.h4(content["highlight2_subtitle"], class_name="text-xl font-semibold text-gray-900 mb-3"),
                            rx.el.p(content["highlight2_content"], class_name="text-gray-700 leading-relaxed text-base mb-10"),
                            class_name="w-9/12",
                        ),

                        # 🎠 Carousel section
                        rx.el.div(
                            carousel_component(
                                images=content["carousel_images"],
                                post_width="300px",
                                image_height="300px",
                                caption=content.get("carousel_caption"),
                            ),
                            class_name="w-full mb-14",
                        ),

                        # 📝 Quote
                        rx.el.div(
                            rx.el.hr(class_name="border-t-2 border-slate-800 w-16 mb-4"),
                            rx.el.p(
                                content["quote"],
                                class_name="text-slate-800 italic text-lg font-medium mb-4",
                            ),
                            rx.el.p(
                                content["quote_author"],
                                class_name="text-gray-600 text-sm",
                            ),
                            class_name="mb-10 w-9/12",
                        ),

                        class_name="px-16 w-full flex flex-col items-center",
                    ),
                    scrollbars="vertical",
                    type="hover",
                    class_name="w-full h-full",
                ),
                class_name="relative bg-white rounded-3xl shadow-xl max-w-xl w-full max-h-[80vh] overflow-hidden flex flex-col",
            ),
            class_name="fixed inset-0 flex items-center justify-center p-4 z-50 bg-black bg-opacity-75",
        ),
        rx.fragment(),
    )



