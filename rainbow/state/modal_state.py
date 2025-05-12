# ------------------------------------
# 🧠 STATE: MODAL STATE
# ------------------------------------
# This file defines the ModalState class to manage session-only pop-up state.
# It handles modals, carousel indices, and like counts — fully in Reflex.


# --- 📦 Imports ---
import reflex as rx
from typing import Dict, List


# --- 🧩 Modal State Logic ---
class ModalState(rx.State):
    """100% Reflex session-like management (no persistence)."""

    active_modal_id: str | None = None
    current_image_index: int = 0
    instagram_image_index: int = 0
    love_counts: Dict[str, int] = {}

    @rx.event
    def open_modal(self, modal_id: str):
        self.active_modal_id = modal_id
        self.current_image_index = 0
        self.instagram_image_index = 0

    @rx.event
    def close_modal(self):
        self.active_modal_id = None

    @rx.event
    def increment_love_count(self, post_id: str):
        self.love_counts[post_id] = self.love_counts.get(post_id, 0) + 1

    @rx.event
    def next_image(self, images: List[str]):
        if len(images) > 1:
            self.current_image_index = (self.current_image_index + 1) % len(images)

    @rx.event
    def prev_image(self, images: List[str]):
        if len(images) > 1:
            self.current_image_index = (self.current_image_index - 1 + len(images)) % len(images)

    @rx.event
    def next_instagram_image(self, images: List[str]):
        if len(images) > 1:
            self.instagram_image_index = (self.instagram_image_index + 1) % len(images)

    @rx.event
    def prev_instagram_image(self, images: List[str]):
        if len(images) > 1:
            self.instagram_image_index = (self.instagram_image_index - 1 + len(images)) % len(images)



# import reflex as rx
# from typing import Dict, List


# class ModalState(rx.State):
#     """100% Reflex session-like management (no persistence)."""

#     active_modal_id: str | None = None
#     current_image_index: int = 0
#     instagram_image_index: int = 0
#     love_counts: Dict[str, int] = {}

#     @rx.event
#     def open_modal(self, modal_id: str):
#         self.active_modal_id = modal_id
#         self.current_image_index = 0
#         self.instagram_image_index = 0

#     @rx.event
#     def close_modal(self):
#         self.active_modal_id = None

#     @rx.event
#     def increment_love_count(self, post_id: str):
#         self.love_counts[post_id] = self.love_counts.get(post_id, 0) + 1

#     @rx.event
#     def next_image(self, images: List[str]):
#         if len(images) > 1:
#             self.current_image_index = (self.current_image_index + 1) % len(images)

#     @rx.event
#     def prev_image(self, images: List[str]):
#         if len(images) > 1:
#             self.current_image_index = (self.current_image_index - 1 + len(images)) % len(images)

#     @rx.event
#     def next_instagram_image(self, images: List[str]):
#         if len(images) > 1:
#             self.instagram_image_index = (self.instagram_image_index + 1) % len(images)

#     @rx.event
#     def prev_instagram_image(self, images: List[str]):
#         if len(images) > 1:
#             self.instagram_image_index = (self.instagram_image_index - 1 + len(images)) % len(images)
