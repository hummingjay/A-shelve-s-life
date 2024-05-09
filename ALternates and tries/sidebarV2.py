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
    MainAxisAlignment,
    IconButton,
    Theme,
    ButtonStyle,
    RoundedRectangleBorder
)
from typing import Any

class SidebarV2(UserControl):
    def __init__(self, app_layout, page):
        super().__init__()
        self.app_layout = app_layout
        self.page = page
        self.nav_items = NavigationRail(
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            min_width=100,
            min_extended_width=400,
            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon_content=FloatingActionButton(icon=icons.HOME, text="Home")
                ),
                NavigationRailDestination(
                    icon_content=self.ContainedIcon(
                        icons.PEOPLE_ALT_OUTLINED,
                        "Patrons",
                    ),
                    selected_icon_content=self.ContainedIcon(
                        icons.PEOPLE_ALT,
                        "Patrons",
                    )
                ),
                NavigationRailDestination(
                    icon_content=self.ContainedIcon(
                        icons.STACKED_BAR_CHART_OUTLINED,
                        "Catalog",
                    ),
                    selected_icon_content=self.ContainedIcon(
                        icons.STACKED_BAR_CHART,
                        "Catalog",
                    )
                ),
                NavigationRailDestination(
                    icon_content=self.ContainedIcon(
                        icons.LIBRARY_BOOKS_OUTLINED,
                        "Circulation",
                    ),
                    selected_icon_content=self.ContainedIcon(
                        icons.LIBRARY_BOOKS_ROUNDED,
                        "Circulation",
                    )
                ),
                NavigationRailDestination(
                    icon_content=self.ContainedIcon(
                        icons.PIE_CHART_OUTLINE,
                        "Work plan",
                    ),
                    selected_icon_content=self.ContainedIcon(
                        icons.PIE_CHART_OUTLINE_ROUNDED,
                        "Work plan",
                    )
                )
            ],
            on_change=lambda e: print("Selected destination:", e.control.selected_index),
            # expand=True,
            extended=True,
            height = 700
        )
    
    def Highlight(self, e):
        pass
    def ContainedIcon(self, icon_name: str, text: str | None = None, action: Any | None = None):
        return Container(
            width=250,
            height=75,
            border_radius=10,
            on_hover=lambda e:self.Highlight(e),
            content=Row(
                    controls=[
                        Column(
                            controls=[
                                Row(
                                    controls=[
                                        IconButton(
                                            icon=icon_name,
                                            icon_size=21,
                                            icon_color=Theme,
                                            style=ButtonStyle(
                                                shape={
                                                    "": RoundedRectangleBorder(radius=10),
                                                },
                                                overlay_color={"": "transparent"},
                                            ),
                                            on_click=action,
                                        ),
                                    ],
                                    alignment=alignment.top_right
                                ),
                                Row(
                                    controls=[
                                        Text(
                                            value=text,
                                            color=Theme,
                                            # size=11,
                                            opacity=1,
                                            animate_opacity=200,
                                        ),
                                    ]  
                                ),
                            ],
                            spacing=0.7,
                            alignment=alignment.top_left
                        )
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
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
                    width=150
                ),
                self.nav_items,
            ], tight=True),
            padding=padding.all(14),
            margin=margin.all(0),
            width=150,
            expand=True
        )
        return self.view