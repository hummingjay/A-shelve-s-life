import flet
from flet import (
    Page,
    Theme,
    PageTransitionsTheme
)

from flet_route import Routing, path
from Home import Home
from About import About
from navigation import bar_item

def main(page:Page):
    page.window_width = 400
    
    theme = Theme()
    theme.page_transitions_linux = PageTransitionsTheme.linux
    page.theme = theme
    page.update()
    
    app_routes = [
        path(
            url="/",
            clear=True,
            view=Home().view
        ),
        path(
            url="/about",
            clear=True,
            view=About().view
        )
    ]
    Routing(
        page=page,
        app_routes=app_routes,
        appbar=bar_item(page)
    )
    page.go(page.route)

flet.app(target=main)