from flet import (
    Page,
    View,
    Text,
    UserControl,
    Column,
    Row,
    Container,
    padding,
)

class Dashboard(UserControl):
    def __init__(self):
        super().__init__()
    
    def my_dash(self):
        return Column([
            Row([
                Container(
                    Text(value="My Dashboard", style="headlineMedium"),
                    expand=True,
                    padding=padding.only(top=15),
                ),
                Container(
                    Text("Here is twhere the content goes!!", weight="bold")
                ),
            ])
        ])
    '''
        return View(
            controls=[
                Text("The Dash Board", weight="bold")
            ]
        )
    '''