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

from sidebar import Sidebar
from Dashboard import Dashboard
from circulation import Circulation
from catalog import Catalog
from patrons import Patrons

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
        
        # page views
        self.Dashboard = Dashboard
        self.circulation = Circulation
        self.catalog = Catalog
        self.patrons = Patrons
        
        
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
    
    def set_page_view(self, i):
        self.active_view = 

