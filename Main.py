import flet
from flet import (
    Page,
    colors,
    UserControl,
    Column,
    Container,
    Row,
    icons,
    IconButton,
    margin, 
    Text,
    AppBar,
    PopupMenuButton,
    PopupMenuItem,
)
from app_layout import AppLayout

class Shelf_life(UserControl):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page
        self.appbar_items = [
            PopupMenuItem(icon=icons.PERSON_OUTLINED, text="Login"),
            PopupMenuItem(), # a divider
            PopupMenuItem(icon=icons.SETTINGS_OUTLINED, text="Settings")
        ]
        self.appbar = AppBar(
            leading=IconButton(icons.MENU),
            leading_width=100,
            title=Text("A Shelf's Life"),
            center_title=False,
            toolbar_height=75,
            bgcolor=colors.LIGHT_BLUE_ACCENT_700,
            actions=[
                Container(
                    content=PopupMenuButton(
                        items=self.appbar_items
                    ),
                    margin=margin.only(left=50, right=25)
                )
            ],
        )
        self.page.appbar = self.appbar
        self.page.update()
    
    def build(self):
        self.layout = AppLayout(
            self,
            self.page,
            tight=True,
            expand=True,
            # vertical_alignment= "start",
        )
        return self.layout



def main(page: Page):
    page.title = "Effimate"
    page.padding = 0
    # page.bgcolor = colors.BLUE_GREY_200
    app = Shelf_life(page)
    page.add(app)
    page.update()

if __name__ == "__main__":
    flet.app(target=main)