#COFFE SHOP
logo = (r'''       
        /~~~~~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
''')
heading = (r'''
   _____ ____  ______ ______ ______ ______ 
  / ____/ __ \|  ____|  ____|  ____|  ____|
 | |   | |  | | |__  | |__  | |__  | |__   
 | |   | |  | |  __| |  __| |  __| |  __|  
 | |___| |__| | |    | |    | |____| |____ 
  \_____\____/|_|    |_|    |______|______|
''')
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
                       },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
"cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
MONEY = 0
RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# Print report.
def print_report(money,resources):
        for key, value in resources.items():
            print(f"{key}: {value}")
        print(f"Money: ${money}")

#  Check resources sufficient?
def resource_check(drink,menu,resources):
    for key, value in menu[drink]["ingredients"].items():
        if value > resources[key]:
            print(f"Sorry! Not enough {key}.")
            return False
    return True

def deducting_resources(drink,menu,resources):
    for key, value in menu[drink]["ingredients"].items():
        resources[key] -= value

    return resources

#  Process coins

def process_payment():
    print("\nPlease insert coins:")

    quarters = float(input("How many quarters? "))
    quarters = quarters * 0.25
    dimes = float(input("How many dimes? "))
    dimes = dimes * 0.10
    nickles = float(input("How many nickles? "))
    nickles = nickles * 0.05
    pennies = float(input("How many pennies? "))
    pennies = pennies * 0.01

    payment = (quarters + dimes + nickles + pennies)
    return payment

#check the payment
def payment_check(drink, menu, cost):

    limit = menu[drink]["cost"]

    if cost > limit:
        change = round((cost - limit), 2)
        print(f"Here is ${change} in change.")
        print(f"Enjoy your {drink}!")
        return limit

    elif cost == limit:
        print(f"Payment Received.\nEnjoy your {drink}!")
        return limit

    elif cost < limit:
        print("Sorry there is not enough Money!. Money refunded")
        cost = 0
        return cost

    return None

def start_coffee_shop(menu, resources, money):

    machine = True
    while machine:
        print(heading)
        print(logo)

      # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
        drink = input("\nWhat would you like? (espresso/latte/cappuccino): " ).lower()

        #  Turn off the Coffee Machine by entering “off” to the prompt 
        if drink == "report" or drink == "off":
            if drink == "off":
                print("Sorry! Machine is off.")
                break
        #prints the report
            if drink == "report":
                print_report(money,resources)
                continue

        if drink not in menu:
            print("This drink is not in our Menu!")
            continue

        #checks if resources are available for making the drink and return true if they are
        available = resource_check(drink, menu, resources)

        
        if available:
            # processes the payment
            payment = process_payment()
            #return what was the final payment
            confirmed_payment = payment_check(drink, menu, payment)
            if confirmed_payment:
                #adds the correct amount in overall money 
                money += confirmed_payment
                # deduct the resources when coffee is completed and update the resources
                resources = deducting_resources(drink, menu, resources)
        else:
            continue

start_coffee_shop(MENU, RESOURCES, MONEY)
