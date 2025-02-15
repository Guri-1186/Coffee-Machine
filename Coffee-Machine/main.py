from src.menu import Menu
from src.drink import Drink
from src.coffee_machine import CoffeeMachine
from src.money_machine import MoneyMachine
from src.admin import Admin
from src.website import open_coffee_website
from pathlib import Path
import traceback

json_file = Path("Coffee-Machine/data/coffee_shop_data.json")

def main():
    try:
        menu = Menu(json_file)
        print(menu.menu_items) 
        coffee_machine = CoffeeMachine(water=300, milk=200, coffee=100)
        money_machine = MoneyMachine()
        admin = Admin(password="CM1186")

        is_on = True
        while is_on:
            choice = input("What would you like? (espresso/latte/cappuccino/americano): ").strip().lower()
            if choice == "off":
                if admin.validate_password():
                    print("Shutting down the coffee machine. Goodbye!")
                    is_on = False
                else:
                    print("You do not have permission to turn off the coffee machine.")

            elif choice == "report":
                coffee_machine.report()
                money_machine.report()

            elif choice == "refill":
                if admin.validate_password():
                    admin.refill_resources(coffee_machine)
                else:
                    print("You do not have permission to refill resources.")

            elif choice in menu.menu_items:
                drink_details = menu.get_drink_details(choice)
                if drink_details:
                    drink = Drink(ingredients=drink_details["ingredients"], cost=drink_details["cost"])
                    if coffee_machine.is_resource_sufficient(drink.ingredients):
                        if money_machine.process_payment(drink.cost):
                            coffee_machine.make_coffee(choice, drink.ingredients)

                            visit_website = input("Would you like to visit the Coffee House website for more choices? (yes/no): ").strip().lower()
                            if visit_website == "yes":
                                open_coffee_website()
                            else:
                                print("Continuing with the coffee machine options.")
            else:
                print("Invalid selection. Please choose a valid drink.")

    except Exception as e:
        print(f"An error occurred: {e}")
        traceback.print_exc()

if __name__ == "__main__":
    main()