
"""Coffee Machine"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 260,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 304,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

print("Welcome to the Coffee machine! ")

def resource_amt(order_ingredients):
    
    is_enough = True
    
    for item in order_ingredients:
       
        if order_ingredients[item] > resources.get(item, 0):
            print(f"Sorry! We do not have enough {item}.")
          
            is_enough = False
    
    return is_enough

def customer_money():
    
    print("Insert your money!")
    
    total = int(input("How many 1 Rupee coin? Type 0 if none --> ")) * 1
    total += int(input("How many 10 Rupees note? Type 0 if none --> ")) * 10
    total += int(input("How many 50 Rupees note? Type 0 if none --> ")) * 50
    total += int(input("How many 100 Rupees note? Type 0 if none --> ")) * 100
    total += int(input("How many 200 Rupees note? Type 0 if none --> ")) * 200
    total += int(input("How many 500 Rupees note? Type 0 if none --> ")) * 500
    total += int(input("How many 2000 Rupees note? Type 0 if none --> ")) * 2000
    
    return total

def transaction(money_rec, drink_cost):
    
    global money
   
    if money_rec >= drink_cost:
        change = round(money_rec - drink_cost, 2)
        print(f"You'll be receiving ₹{change} amount of change.")
        money += drink_cost
     
        return True
  
    else:
        print("Sorry! You do not have enough money.")
      
        return False

def make_coffee(drink):
    
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]

machine_on = True

while machine_on:
    
    user_choice = input("We have -> 1.Espresso 2.Latte 3.Cappuccino.\nWhat would you like to have? ---> ").lower()

    if user_choice == "off":
        
        machine_on = False
    
    elif user_choice == "report":
        
        print("money: ₹", money)
        print("water: ", resources["water"], "ml")
        print("milk: ", resources["milk"], "ml")
        print("coffee: ", resources["coffee"], "g")
    
    elif user_choice in MENU:
        drink = MENU[user_choice]
        
        if resource_amt(drink["ingredients"]):
            payment = customer_money()
            
            if transaction(payment, drink["cost"]):
                make_coffee(drink)
   
    else:
        print("Invalid choice. Please select a valid option.")


