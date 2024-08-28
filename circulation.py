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
        return Text("The Circulation", weight="bold")