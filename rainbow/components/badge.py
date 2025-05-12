# ------------------------------------
# ℹ️ COMPONENT: REFLEX BADGE
# ------------------------------------
# This file defines a persistent "Built with Reflex" badge.
# It uses a tooltip (`hint`) and links to the Reflex GitHub repo.
# The style adapts to dark and light modes.


# --- 📦 Imports ---
import reflex as rx

# 🧩 Components
from rainbow.components.icons import get_icon
from rainbow.state.badge_state import BadgeState
# from rainbow.components.hint import hint


# --- 🏷️ Reflex Badge (Created my own badge) ---
def badge() -> rx.Component:
    return rx.el.div(
        rx.link(
            rx.el.div(
                get_icon("badge_logo"),
                # rx.el.img(
                #     src="/images/lucille_logo.png",
                #     class_name="h-4 w-4 sm:h-6 sm:w-6",
                # ),
                rx.el.span(
                    "Built with Reflex",
                    class_name="ml-[4px] sm:ml-[6px] font-semibold text-xs sm:text-sm whitespace-nowrap",
                ),
                class_name=rx.cond(
                    BadgeState.is_hovered,
                    rx.color_mode_cond(
                        light="flex items-center px-2 py-2 sm:pt-1 sm:pb-1 pr-2 sm:pr-2 bg-black text-white border border-black/20 rounded-lg transition-all duration-300 transform hover:scale-105",
                        dark="flex items-center px-2 py-2 sm:pt-1 sm:pb-1 pr-2 sm:pr-2 bg-white text-black border border-white/20 rounded-lg transition-all duration-300 transform hover:scale-105",
                    ),
                    rx.color_mode_cond(
                        light="flex items-center px-2 py-2 sm:pt-1 sm:pb-1 pr-2 sm:pr-2 bg-white/80 text-black border border-black/10 rounded-lg transition-all duration-300 backdrop-blur",
                        dark="flex items-center px-2 py-2 sm:pt-1 sm:pb-1 pr-2 sm:pr-2 bg-white/5 text-white border border-white/10 rounded-lg transition-all duration-300 backdrop-blur",
                    ),
                ),
                on_mouse_enter=BadgeState.handle_mouse_enter,
                on_mouse_leave=BadgeState.handle_mouse_leave,
            ),
            href="https://github.com/reflex-dev/reflex-web",
            is_external=True,
            class_name="no-underline",
        ),
        class_name="fixed bottom-4 right-4 z-50",  # Bottom right corner
    )



# --- 🏷️ Reflex Badge ---
# @rx.memo
# def badge() -> rx.Component:
#     return hint(
#         text="This entire website was made with Reflex!",
#         content=rx.link(
#             get_icon("badge_logo"),
#             rx.text(
#                 "Built with Reflex",
#                 font_family="Didact Gothic",
#                 color=rx.color_mode_cond(
#                     light="black",
#                     dark="white",
#                 ),
#                 text_decoration="none",
#                 class_name="text-slate-1 font-semibold font-['Instrument_Sans'] text-sm leading-4 tracking-[-0.00656rem]",
#             ),
#             underline="none",
#             class_name=rx.color_mode_cond(
#                 light="fixed bottom-6 right-6 flex flex-row gap-1.5 items-center w-auto rounded-lg bg-[#FCFCFD] shadow-small p-1.5 transition-bg border border-solid border-[#E0E1E6] z-[9998] cursor-pointer",
#                 dark="fixed bottom-6 right-6 flex flex-row gap-1.5 items-center w-auto rounded-lg bg-[#151618] shadow-small p-1.5 transition-bg border border-solid border-[#27282B] z-[9998] cursor-pointer",
#             ),
#             href="https://github.com/reflex-dev/reflex-web",
#             is_external=True,
#         ),
#         align="start",
#     )

