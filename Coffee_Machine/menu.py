class MenuItem:
    """
    Simple class to instantiate a menu item
    Contains the constructor for an item in the coffee machine
    """

    def __init__(self,name,water,milk,coffee,cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

class Menu:
    """
    Object for the menu with the drink constructed
    """
    # Constructor
    def __init__(self):
        self.menu = [
            MenuItem(name="latte", water=200, milk=150, coffee=24, cost=2.5),
            MenuItem(name="espresso", water=50, milk=0, coffee=18, cost=1.5),
            MenuItem(name="cappuccino", water=250, milk=100, coffee=24, cost=3.0)
        ]

    # getter methods
    def find_items(self):
        # return all items of the menu
        options=""
        for item in self.menu:
            options += f"{item.name}/"
        return options

    def find_drink(self, order_name):
        # search the menu for the ordered item
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available!")