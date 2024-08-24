from flet import (
    Page,
    View,
    Text,
    UserControl
)

class Dashboard(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self):
        return View(
            controls=[
                Text("The Dash Board", weight="bold")
            ]
        )