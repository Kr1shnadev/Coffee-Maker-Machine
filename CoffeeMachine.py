from menu import resources,menu
def print_format(resource,savings):
    milk = resource["milk"]
    coffee = resource["coffee"]
    water = resource["water"]

    print(f"""
    Water:{water} ml
    Milk:{milk} ml
    Coffee:{coffee} g
    Savings:$ {savings}""")

def resource_check(coffee, machine):
    if machine["water"] < coffee["water"]:
        print("Sorry! We ran out of water .")
        return False
    if machine["milk"] < coffee["milk"]:
        print("Sorry! We ran out of milk 🥛.")
        return False
    if machine["coffee"] < coffee["coffee"]:
        print("Sorry! We ran out of coffee powder.")
        return False
    return True  # Enough resources available

def make_coffee(coffee, machine,input):
    machine["water"] -= coffee["water"]
    machine["milk"] -= coffee["milk"]
    machine["coffee"] -= coffee["coffee"]
    print(f"Here is your {input} 🍵. Enjoy! ")
    return machine

def coin_process(price,savings):
    print("Insert coins 🪙.")
    pennies=int(input("Insert pennies: "))
    nickels = int(input("Insert nickels: "))
    dimes = int(input("Insert dimes: "))
    quarters = int(input("Insert quarters: "))

    total_coin_entered= (pennies*0.01)+(dimes*0.05)+(nickels*.10)+(quarters*0.25)

    if total_coin_entered<price:
        print("Sorry that's not enough money. Money refunded")
        return False
    elif total_coin_entered>price:
        change = total_coin_entered - price
        print(f"Here is Your $ {change:.2f} change.")
        savings+=price
        make_coffee(choice, resources, user_input)
        return savings
    else:
        savings+=price
        make_coffee(choice, resources, user_input)
        return savings

on=True
savings = 0
while(on):
    user_input=input("\nWhat would you like? (espresso/latte/cappuccino):").lower()
    if user_input=="off":
        print("-------<<<Shutting down Coffee machine>>>-------")
        on=False
    elif user_input=="report":
        print_format(resources,savings)
    elif user_input in ["latte", "cappuccino", "espresso"]:
        cost=menu[user_input]["cost"]
        print(f"Price: $ {cost}")
        choice=menu[user_input]["ingredients"]
        milk = choice["milk"]
        water = choice["water"]
        coffee = choice["coffee"]

        if resource_check(choice,resources)==True:
            savings=coin_process(cost,savings)
    else:
        print("Wrong input!")







