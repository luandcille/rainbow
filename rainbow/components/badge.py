import reflex as rx
from rainbow.components.icons import get_icon
from rainbow.components.hint import hint

@rx.memo
def badge() -> rx.Component:
    return hint(
        text="This entire website was made with Reflex!",
        content=rx.link(
            get_icon("badge_logo"),
            rx.text(
                "Built with Reflex", 
                font_family="Didact Gothic",
                color=rx.color_mode_cond(
                    light="black",  # Text color in light mode
                    dark="white",   # Text color in dark mode
                ),
                text_decoration="none",
                class_name="text-slate-1 font-semibold font-['Instrument_Sans'] text-sm leading-4 tracking-[-0.00656rem]",
            ),
            underline="none",
            class_name=rx.color_mode_cond(
                light="fixed bottom-6 right-6 flex flex-row gap-1.5 items-center w-auto rounded-lg bg-[#FCFCFD] shadow-small p-1.5 transition-bg border border-solid border-[#E0E1E6] z-[9998] cursor-pointer",
                dark="fixed bottom-6 right-6 flex flex-row gap-1.5 items-center w-auto rounded-lg bg-[#151618] shadow-small p-1.5 transition-bg border border-solid border-[#27282B] z-[9998] cursor-pointer",
            ),
            href="https://github.com/reflex-dev/reflex-web",
            is_external=True
        ),
        align="start",
    )
