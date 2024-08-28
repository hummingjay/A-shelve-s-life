from typing import TYPE_CHECKING
if TYPE_CHECKING:
    # from user import User
    #from item import Item
    from circulation import Circulation
    from catalog import Catalog
    # from Dashboard import Dashboard
    from patrons import Patrons

# shall define the class as I go along adding any new function
class DataStore:
    """
        this is an abstract class to define the structure for
        subclasses therefore if you forget to define it fails to run
        raising the error
    """
    def add_patron(self, details) -> None:
        raise NotImplementedError
    
    def get_patron(self, id) -> "Patrons":
        raise NotImplementedError
    
    # def add_item(self, )