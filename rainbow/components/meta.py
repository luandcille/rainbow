import reflex as rx

meta_tags = [
    # HTML Meta Tags
    {"name": "application-name", "content": "Lucille Vigné"},
    {
        "name": "keywords",
        "content": "reflex, python, web apps, lucille vigné, aesthetic, notion",
    },
    {
        "name": "description",
        "content": "Beneath the Rainbow Sky",
    },
]

def favicons_links() -> list[rx.Component]:
    return [
        rx.el.link(rel="icon", type="image/png", sizes="16x16", href="images/lucille_logo_16.png"),
        # rx.el.link(rel="icon", type="image/png", sizes="32x32", href="images/lucille_logo_32.png"),
        
    ]
