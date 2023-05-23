# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# emojis = {
#     "coffee": ☕
#     "coins": 💰
# }

# ******************************************* FUNCTIONS **************************************************


def print_report(funds, resources):
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${funds}")


def check_resources(drink):
    sufficient = True
    # TODO: get the resources required for the drink dictionary
    # TODO: compare each key to the remaining resources
    for resource in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][resource] < resources[resource]:
            sufficient = True
        else:
            sufficient = False
            return sufficient, resource
    return sufficient, resource


def process_payment(drink, funds, resources):
    cost = MENU[drink]["cost"]
    print(f"The cost of your drink is: {cost}. Please enter coins. ")
    quarters = int(input("How many quarters?:  "))
    dimes = int(input("How many dimes?:  "))
    nickles = int(input("How many nickles?:  "))
    pennies = int(input("How many pennies?: "))
    tender = ((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    enough_tender = True
    if tender > cost:
        change = round((tender - cost), 2)
        print(f"Here is your change. ${change}")
    if tender < cost:
        enough_tender = False
    else:
        funds += cost
        for ingredient in MENU[drink]['ingredients']:
            resources[ingredient] = resources[ingredient] - MENU[drink]["ingredients"][ingredient]
    return funds, resources, enough_tender


# ****************************************** GLOBAL VARIABLES ***************************************


funds = 0
end_program = False

while not end_program:
    # TODO: User input to ask what kind of coffee they want.
    drink = input("     What would you like? (espresso/latte/cappuccino):  ").lower()

    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        # TODO: BUG!! Does not tell user there is insufficient resource before asking for payment
        make_drink, resource_limit = check_resources(drink)
        if make_drink:
            funds, resources, enough_tender = process_payment(drink, funds, resources)
            if enough_tender:
                print(f"Here is your {drink}.  Enjoy! ")
            else:
                print("Sorry, that's not enough money. Money refunded.  ")
        else:
            print(f"Sorry, there is not enough {resource_limit}.")
            end_program = True
    elif drink == 'report':
        print_report(funds, resources)
    elif drink == 'off':
        end_program = True
    else:
        "You have not made a valid selection. "

'''
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
'''
