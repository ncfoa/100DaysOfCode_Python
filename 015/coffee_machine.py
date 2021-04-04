# Coffee Machine

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
    "money": 0
}


def deliver():
    coffee = '''
        (  )   (   )  )
         ) (   )  (  (
         ( )  (    ) )
         _____________
        <_____________> ___
        |             |/ _ \\
        |    Good       | | |
        |    Java       |_| |
     ___|             |\\___/
    /    \\___________/    \\
    \\_____________________/
    '''
    print(coffee)


def start():
    global resources
    choice = input("What drink would you like? 'espresso', 'latte', 'cappuccino': ")
    if choice in MENU:
        if not check_supplies(MENU[choice]["ingredients"]):
            print(f"Not enough ingredients for {choice} please resupply.")
            start()
        if not enter_coins(choice):
            start()
        else:
            make_drink(choice)
            deliver()
            print("Enjoy your beverage")
            start()
    elif choice == "report":
        print(f' Water: {resources["water"]}')
        print(f' Milk: {resources["milk"]}')
        print(f' Coffee: {resources["coffee"]}')
        print(f' Money: ${"{:.2f}".format(resources["money"])}')
        start()
    elif choice == "resupply":
        resupply()
        start()
    elif choice == "off":
        print("Powering OFF Coffee Machine")
        exit(0)
    else:
        print(f"Error {choice} not understood ")
        start()


def enter_coins(drink):
    global resources
    quarters = input("How many quarters? ")
    dimes = input("How many dimes? ")
    nickles = input("How many nickles? ")
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    money = 0

    if quarters:
        money += int(quarters) * quarter
    if dimes:
        money += int(dimes) * dime
    if nickles:
        money += int(nickles) * nickle
    if money < MENU[drink]["cost"]:
        refund = "{:.2f}".format(money)
        print(f'{drink} costs ${"{:.2f}".format(MENU[drink]["cost"])}')
        print(f'Not enough money. Refunding ${refund}')
        money = 0
        return False
    elif money > MENU[drink]["cost"]:
        resources["money"] = MENU[drink]["cost"]
        money -= MENU[drink]["cost"]
        change = "{:.2f}".format(money)
        print("Thank You...")
        print(f"Making Change ${change}")
        money = 0
        return True
    else:
        money = 0
        resources["money"] = int(MENU[drink]["cost"])
        print("Thank You...")
        return True


def check_supplies(materials):
    global resources
    for item in materials:
        if resources[item] < materials[item]:
            return False
        else:
            return True


def make_drink(drink):
    global resources
    for i in MENU[drink]["ingredients"]:
        resources[i] -= MENU[drink]["ingredients"][i]
    return True


def resupply():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


start()
