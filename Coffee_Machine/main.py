from coffee_data import *
import sys



def check_resources(name):
    # check the available resource -> negative == return false
    for resource in MENU[name]["ingredients"]:
        checkResource = resources[resource] - MENU[name]["ingredients"][resource]
        if checkResource < 0:
            return False, resource
    return True, None

def process_transaction(name, total_money):
    # perform a check on resources -> return true or false
    isResourceAvailable, missingResoure = check_resources(name)

    if isResourceAvailable == False:
        print("sorry, there is not enough %s" % missingResoure)
    else:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))*0.25
        dimes = int(input("How many dimes?: "))*0.10
        nickles = int(input("How many nickles?: "))*0.05
        pennies = int(input("How many pennies?: "))*0.01
        total_money_input = quarters+dimes+nickles+pennies

        if total_money_input < MENU[name]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            # update resource and caluclate the refunded money
            for resource in MENU[name]["ingredients"]:
                resources[resource] -= MENU[name]["ingredients"][resource]

            refunded_value = round((total_money_input - MENU[name]["cost"]),2)

            if refunded_value == 0:
                print("Here is your %s ☕. Enjoy!" % name)
                total_money += MENU[name]["cost"]
                total_money = round(total_money,2)
                return total_money
            elif refunded_value > 0:
                print("Here is $%s in change" % refunded_value)
                print("Here is your %s ☕. Enjoy!" % name)
                total_money += MENU[name]["cost"]
                total_money = round(total_money,2)
                return total_money


if __name__ == '__main__':
    # start the coffee machine with total money
    total_money = 100

    while True:
        userInput = input("What would you like? (espresso/latte/cappuccino): ")

        if userInput in ["quit","exit"]:
            print("Have a nice day!")
            sys.exit()

        # report function
        elif userInput == "report":
            for resource in resources:
                if resource == "coffee":
                    print("%s : %sg" % (resource.capitalize(), resources[resource]))
                else:
                    print("%s : %sml" % (resource.capitalize(), resources[resource]))
            print("%s : $%s" % ("Money", total_money))

        # report function
        elif userInput in ["espresso","latte","cappuccino"]:
            # update the machine remaining balance
            money = process_transaction(userInput, total_money)
            total_money=money
        else:
            print("Invalid Input!")