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
    VerticalDivider,
)
from flet_route import Routing, path
from sidebar import Sidebar
from Dashboard import Dashboard
from circulation import Circulation
from catalog import Catalog
from patrons import Patrons
# from app_logic import Page_change

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
        self.sidebar = Sidebar(self, page)
        self.current_view = pages
        
        pages = [
            path(url ="/", clear=True, view=Dashboard),
            path(url="/Patrons", clear=True, view=Patrons),
            path(url="/Catalog", clear=True, view=Catalog),
            path(url="/circulation", clear = True, view = Circulation)
        ]
        
        Routing(page=page,
                app_routes=pages)
        page.go(page.route)
        
        '''
        self._active_view: Control = Column(
            controls=[
                Page_change(self.sidebar.nav_items.on_change),
                # self.update()
                # self.sidebar.nav_items.on_change
            ],
            alignment="center",
            horizontal_alignment="center",
            expand=True
        )
        '''
        
        self.controls = [
            self.sidebar,
            VerticalDivider(width=1),
            # self.active_view
            self.current_view
        ]
    
    @property
    def active_view(self):
        return self._active_view
    
    @active_view.setter
    def active_view(self, view):
        self._active_view = view
        self.update()

