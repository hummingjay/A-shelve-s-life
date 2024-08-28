from flet import (
    Page,
    View,
    Text,
    UserControl
)

class Catalog(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self):
        return Text("Our Catalog", weight="bold")