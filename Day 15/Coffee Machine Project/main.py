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

profit = 0

def resources_sufficient(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"There's not enough {item}.")
            return False
    return True

def process_coins():
    print("Enter the amount")
    amount = int(input("Enter the amount of quarters: ")) * 0.25
    amount += int(input("Enter the amount of dimes: ")) * 0.10
    amount += int(input("Enter the amount of nickels: ")) * 0.05
    amount += int(input("Enter the amount of pennies: ")) * 0.01
    return amount

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here's your drink, {drink_name}. ☕ Enjoy your drink!")

coffee_is_on = True

while coffee_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == "off":
        print("Goodbye!")
        coffee_is_on = False
    elif user_input == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[user_input]
        if resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink["ingredients"])
