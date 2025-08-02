import menu
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#intializing classes
cafe_menu = Menu()
coffee_machine = CoffeeMaker()
administration = MoneyMachine()

is_on = True
while is_on:

    options =cafe_menu.get_items()
    choice = input(f"\nWhat would you like to drink ({options})? : ")
    if choice == "report":
        #prints the resources
        coffee_machine.report()
        #prints the money
        administration.report()

    elif choice == "off":
        print("Sorry! Machine is off")
        order = False

    drink = cafe_menu.find_drink(choice)

    available = coffee_machine.is_resource_sufficient(drink)
    if available:

        confirmed_payment = administration.make_payment(drink.cost)
        if confirmed_payment:
            coffee_machine.make_coffee(drink)

