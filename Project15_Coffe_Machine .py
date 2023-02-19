from time import sleep
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
    "milk": 100,
    "coffee": 100,
}

def resources_sufficients(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    print("Insert amount coins")
    total = int(input("Quarters: ")) * 0.25
    total += int(input("Dimes: ")) * 0.1
    total += int(input("Nickles: ")) * 0.05
    total += int(input("pennies: ")) * 0.01
    return total

def transaction_sucessful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Insufficient moneyn. Money refunded")
        return False

def make_coffe(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f'Here is your {drink}! :)')



profit = 0
on = True
while on:
    choice = input("espresso/latte/cappuccino: ")
    if choice == "off":
        print("turning off...")
        sleep(1)
        print("OFF")
        on = False
    elif choice == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffe: {resources["coffee"]}g')
        print(f'Money: ${profit}')
    else:
        drink = MENU[choice]
        if resources_sufficients(drink["ingredients"]):
            payment = process_coins()
            if transaction_sucessful(payment, drink["cost"]):
                make_coffe(choice, drink["ingredients"])

        


