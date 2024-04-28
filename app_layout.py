from flet import (
    Control,
    Column,
    Container,
    IconButton,
    Page,
    Row,
    Text,
    colors,
    icons,
    VerticalDivider
)
from sidebar import Sidebar

class AppLayout(Row):
    """
        Layout of app in class inheriting from Row control
    """
    def __init__(
        self,
        app,
        page: Page,
        *args,
        **kwargs  
    ):
        super().__init__(*args, **kwargs)
        self.app = app
        self.page = page
        '''
        self.toggle_nav_rail_button = IconButton(
            icon=icons.MENU_OUTLINED,
            icon_color=colors.BLUE_GREY_400,
            selected=False,
            on_click=self.toggle_nav_rail
        )
        '''
        self.sidebar = Sidebar(self, page)
        self._active_view: Control = Column(
            controls=[
                Text("Active View")
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True
        )
        self.controls = [
            self.sidebar,
            VerticalDivider(width=1),
            self.active_view
        ]
    
    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()
    '''
    def toggle_nav_rail(self, e):
        self.sidebar.visible = not self.sidebar.visible
        self.toggle_nav_rail_button.selected = not self.toggle_nav_rail_button.selected
        self.page.update()
    '''