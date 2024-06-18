from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_mchine = MoneyMachine()
turn_on = True
while turn_on:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()
    if choice == "off":
        print("Machine Turned Off!!")
        turn_on = False
    elif choice == "report":
        coffee_maker.report()
        money_mchine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_mchine.make_payment(
            drink.cost
        ):
            coffee_maker.make_coffee(drink)
