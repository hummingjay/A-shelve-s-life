from flet import (
    Page,
    View,
    Text,
    UserControl
)

class Patrons(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self):
        return Text("Our Patrons", weight="bold")