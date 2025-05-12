import reflex as rx


class BadgeState(rx.State):
    is_hovered: bool = False
    badge_source: str = (
        'import reflex as rx\nfrom app.states.badge_state import BadgeState\n\ndef badge() -> rx.Component:\n    return rx.el.div(\n        rx.el.div(\n            rx.el.img(\n                src="/simple_clean_pytherin.webp",\n                class_name="h-6 w-6",\n            ),\n            rx.el.span(\n                "Built with Pytherin",\n                class_name="ml-2 font-medium text-sm",\n            ),\n            class_name=rx.cond(\n                BadgeState.is_hovered,\n                "flex items-center px-3 py-2 bg-gray-600/90 text-white rounded-lg transition-all duration-300 transform hover:scale-105",\n                "flex items-center px-3 py-2 bg-gray-600/80 text-white rounded-lg transition-all duration-300",\n            ),\n            on_mouse_enter=BadgeState.handle_mouse_enter,\n            on_mouse_leave=BadgeState.handle_mouse_leave,\n        ),\n        class_name="inline-block",\n    )'
    )

    @rx.event
    def handle_mouse_enter(self):
        self.is_hovered = True

    @rx.event
    def handle_mouse_leave(self):
        self.is_hovered = False