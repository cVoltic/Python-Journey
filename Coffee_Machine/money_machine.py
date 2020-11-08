class MoneyMachine:
    """
    Class that mange payment (acceptable cash/machine total) and refunds
    """
    # global class variables
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    # constructor
    def __init__(self):
        self.__profit = 0
        self.__money_received = 0

    # getter methods
    def report(self):
        # print the current profit amount
        print("%s : $%s" % ("Money", self.__profit))

    def process_coins(self):
        # process the handling of the input coins
        print("Please insert coins.")
        for coin in self.COIN_VALUES:
            self.__money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
        return self.__money_received

    def make_payment(self, cost):
        # check against the order and process refund if payment is above the refund
        self.process_coins()
        if self.__money_received >= cost:
            change = round(self.__money_received - cost,2)
            print("Here is $%s in change" % change)
            self.__profit += cost
            self.__money_received = 0
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            self.__money_received = 0
            return False
