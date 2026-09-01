# rxconfig.py
import os
import reflex as rx
from reflex.plugins.sitemap import SitemapPlugin
from reflex.plugins import TailwindV4Plugin

config = rx.Config(
    app_name="rainbow",
    api_url=os.getenv("API_URL", "http://127.0.0.1:8000"), 
    plugins=[
        SitemapPlugin(),
        TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(),
    ],
)
