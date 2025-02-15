class CoffeeMachine:
    def __init__(self, water, milk, coffee):
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }

    def is_resource_sufficient(self, order_ingredients):
        for ingredient in order_ingredients:
            if order_ingredients[ingredient] > self.resources.get(ingredient, 0):
                print(f"Sorry, there is not enough {ingredient}.")
                return False
        return True

    def make_coffee(self, drink_name, order_ingredients):
        for ingredient in order_ingredients:
            self.resources[ingredient] -= order_ingredients[ingredient]
        print(f"Here is your {drink_name} ☕️. Enjoy!")

    def report(self):
        print(f"Water: {self.resources['water']}ml")
        print(f"Milk: {self.resources['milk']}ml")
        print(f"Coffee: {self.resources['coffee']}g")