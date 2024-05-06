from flet import(
    UserControl,
    NavigationRailLabelType,
    NavigationRail,
    FloatingActionButton,
    NavigationRailDestination,
    icons,
    Icon,
    Column,
    Container,
    Row,
    Text,
    FontWeight,
    colors,
    border_radius,
    alignment,
    padding,
    margin,
    MainAxisAlignment
)
from typing import Any

class Sidebar(UserControl):
    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.nav_items = NavigationRail(
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            leading=FloatingActionButton(icon=icons.HOME, text="Home"),
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=icons.PEOPLE_ALT_OUTLINED,
                    selected_icon=icons.PEOPLE_ALT,
                    label="Patrons"
                ),
                NavigationRailDestination(
                    icon=icons.STACKED_BAR_CHART_OUTLINED,
                    selected_icon_content=Icon(icons.STACKED_BAR_CHART),
                    label="Catalog"
                ),
                NavigationRailDestination(
                    icon=icons.LIBRARY_BOOKS_OUTLINED,
                    selected_icon_content=Icon(icons.LIBRARY_BOOKS_ROUNDED),
                    label_content=Text("Circulation"),
                )
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
            # expand=True,
            extended=True,
            height = 700
        )
    
    
    def build(self):
        self.view = Container(
            content=Column([
                Row([
                    Text("Menu", size=21, weight=FontWeight.BOLD)
                ], alignment=MainAxisAlignment.CENTER),
                # divider
                Container(
                    bgcolor=colors.BLACK26,
                    border_radius=border_radius.all(30),
                    height=1,
                    alignment=alignment.center_right,
                    width=200
                ),
                self.nav_items,
            ], tight=True),
            padding=padding.all(7),
            margin=margin.all(0),
            width=200,
            expand=True
        )
        return self.view