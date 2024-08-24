from flet import (
    Page,
    View,
    Text,
    UserControl
)

class Circulation(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self):
        return View(
            controls=[
                Text("The Circulation", weight="bold")
            ]
        )