# ------------------------------------
# ℹ️ META TAGS CONFIGURATION
# ------------------------------------
# This file defines all meta tags for Lucille Vigné’s personal site.
# It includes standard HTML meta info and Open Graph tags for link previews.


# --- 🏷️ Meta Tags ---
meta_tags = [
    # 🔤 HTML Meta Tags
    {"name": "application-name", "content": "Lucille Vigné"},
    {
        "name": "keywords",
        "content": "reflex, python, web apps, lucille vigné, aesthetic, notion",
    },
    {
        "name": "description",
        "content": "Beneath the Rainbow Sky",
    },

    # 🔗 Open Graph Meta Tags (for social media preview)
    {"property": "og:url", "content": "https://lucillevigne.com"},
    {"property": "og:type", "content": "website"},
    {"property": "og:title", "content": "Lucille Vigné · Beneath the Rainbow Sky"},
    {
        "property": "og:description",
        "content": (
            "A creative and visionary space where ideas shine as brightly as rainbows, "
            "inspiring imagination and limitless possibilities."
        ),
    },
    {"property": "og:image", "content": "/previews/lucille_vigne_rainbow.png"},
]
