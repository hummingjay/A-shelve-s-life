from flet import (
    Page,
    View,
    Text,
    UserControl
)
from flet_route import Params, Basket

class Circulation(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self, page:Page, params:Params, basket:Basket):
        return View(
            controls=[
                Text("The Circulation", weight="bold")
            ]
        )