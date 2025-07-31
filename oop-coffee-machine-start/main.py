from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

drinks = Menu()
coffee_machine = CoffeeMaker()
profit = MoneyMachine()

is_on = True
while is_on:
    options = drinks.get_items()
    order = input("What would you like?" + f" ({options}): ")
    if order == "report":
        coffee_machine.report()
        profit.report()
    elif order == "off":
        is_on = False
    else:
        beverage = drinks.find_drink(order)
        if coffee_machine.is_resource_sufficient(beverage):
            if profit.make_payment(beverage.cost):
                coffee_machine.make_coffee(beverage)
