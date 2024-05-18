from flet import (
    Row,
    Text,
)

def Page_change(value):
    if value == 0:
        print("Patrons")
        return Row(
            controls=[
                Text("Patrons")
            ]
        )
    if value == 1:
        print("Catalog")
        return Row(
            controls=[
                Text("Catalog")
            ]
        )
    if value == 2:
        print("Circulation")
        return Row(
            controls=[
                Text("Circulation")
            ]
        )
    
    else:
        print(value)
        return Row(
            controls=[
                Text("Default page?")
            ]
        )
