# ------------------------------------
# ℹ️ DATA: PRODUCT PROJECTS
# ------------------------------------
# This file defines all product-related projects displayed in the portfolio.
# Each project contains metadata including title, description, visuals, tags, and timeline.


# --- 📦 Typing ---
from typing import List, TypedDict


class Project(TypedDict):
    title: str
    description: str
    date_range: str
    image_url: str
    tags: List[str]
    link: str


# --- 🚀 Product Section Title ---
product_section_title = "built, co-founded to infinity... and beyond"


# --- 🧪 Product Projects List ---
product_projects: List[Project] = [
     {
            "title": "i love to tour",
            "description": "A community-driven archive of Michael Jackson’s tours and performances, where fans can explore, connect, follow each other, and earn points along the way",
            "image_url": "/images/i-love-to-tour.png",
            "tags": ["founder", "web app"],
            "link": "https://i-love-to-tour.vercel.app/",
            "date_range": "2025 / 2026",
        },

    {
        "title": "aesthetic",
        "description": "Make your Notion titles pop with that creative extension. Customize your headings like never before, adding a unique touch to your digital space",
        "image_url": "/images/aesthetic.png",
        "tags": ["founder", "extension"],
        "link": "https://chromewebstore.google.com/detail/aesthetic-notion-styled/npgghjedpchajflknnbngajkjkdhncdo",
        "date_range": "August 2024",
    },
    # {
    #     "title": "kwotes app",
    #     "description": "Kwotes offers a vast collection of inspiring quotes. Easily explore, save, and share your favorites, making daily motivation and insight just a tap away",
    #     "image_url": "/images/kwotes.png",
    #     "tags": ["co-founder", "mobile app"],
    #     "link": "https://kwotes.fr",
    #     "date_range": "April 2024",
    # },
    {
        "title": "la zébrelle",
        "description": "The Savannah is an educational platform that promotes awareness, celebrates the diversity of neurodiversity, fostering inclusion and understanding for all",
        "image_url": "/images/la_zebrelle.png",
        "tags": ["founder", "educational platform"],
        "link": "https://lazebrelle.fr",
        "date_range": "November 2019",
    },
    {
        "title": "africa vivre",
        "description": "Embrace Africa's rich cultural diversity and support local artisans. Discover unique, handcrafted products made with passion and tradition",
        "image_url": "/images/africa_vivre.png",
        "tags": ["associate", "marketplace"],
        "link": "https://www.africavivre.com",
        "date_range": "April 2016",
    },
]
