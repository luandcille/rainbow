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
                color="black",
                text_decoration="none",
                weight="medium",
                class_name="text-slate-1 font-semibold font-['Instrument_Sans'] text-sm leading-4 tracking-[-0.00656rem]",
            ),
            underline="none",
            class_name="fixed bottom-4 right-4 flex flex-row gap-1.5 items-center w-auto rounded-lg dark:bg-[#FCFCFD] shadow-small p-1.5 transition-bg border border-solid dark:border-[#E0E1E6] z-[9998] bg-[#151618] border-[#27282B] cursor-pointer",
            href="https://github.com/reflex-dev/reflex-web",
        ),
        align="start",
    )