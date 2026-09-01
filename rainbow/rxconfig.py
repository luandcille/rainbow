import reflex as rx

config = rx.Config(
    app_name="rainbow",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)