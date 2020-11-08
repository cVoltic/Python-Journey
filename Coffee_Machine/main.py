##transpose to OOP
from menu import *
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import sys
if __name__ == '__main__':

    #instantiate the objects
    menu = Menu()
    coffee_engine = CoffeeMaker()
    money_engine = MoneyMachine()


    while True:
        userInput = input(f"What would you like? ({menu.find_items()}): ")

        if userInput in ["quit","exit","off"]:
            print("Have a nice day!")
            sys.exit()

        # report function
        elif userInput == "report":
            coffee_engine.report()
            money_engine.report()

        # order function
        else:
            # get the user order
            # first check to see if the machine can make
            order = menu.find_drink(userInput)
            can_make = coffee_engine.is_resource_sufficient(order)
            if can_make:
                # if we can make it, then ask the user to input the coins for processing
                payment_made = money_engine.make_payment(order.cost)
                if payment_made:
                    coffee_engine.make_coffee(order)
