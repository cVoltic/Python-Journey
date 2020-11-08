class CoffeeMaker:
    """
    Class that holds the resource and check to see if we can make the coffee
    """

    def __init__(self):
        self.__resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    # getter methods
    def report(self):
        # print the available resources int the coffee machine
        for resource in self.__resources:
            if resource == "coffee":
                print("%s : %sg" % (resource.capitalize(), self.__resources[resource]))
            else:
                print("%s : %sml" % (resource.capitalize(), self.__resources[resource]))

    # class methods for brewing the coffee
    def is_resource_sufficient(self, drink):
        # check the coffee machine to see if the available resource is sufficient
        # takes in the drink object from menu
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.__resources[item]:
                print("sorry, there is not enough %s" % item)
                can_make = False
                return can_make
        return can_make

    def make_coffee(self, order):
        # deduct the available resources to make the coffee
        for item in order.ingredients:
            self.__resources[item] -= order.ingredients[item]
        print("Here is your %s ☕. Enjoy!" % order.name)
