
class MoneyMachine:
    CURRENCY = "GEL"
    def __init__(self):
        self.profit = 0
    def process_payment(self, drink_cost):
        payment_method = input("How would you like to pay? (cash or card): ").strip().lower()
        if payment_method == "card":
            print(f"Please pay {MoneyMachine.CURRENCY} {drink_cost:.2f} with your card.")
            self.profit += drink_cost  
            return True
        elif payment_method == "cash":
            try:
                cash_received = float(input(f"Please insert cash. The total is {MoneyMachine.CURRENCY} {drink_cost:.2f}: "))
                if cash_received >= drink_cost:
                    change = round(cash_received - drink_cost, 2)
                    if change > 0:
                        print(f"Here is {MoneyMachine.CURRENCY} {change:.2f} in change.")
                    self.profit += drink_cost
                    return True
                else:
                    print("Sorry, that's not enough money. Money refunded.")
                    return False
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
                return False
        else:  
            print("Invalid payment method. Please choose 'cash' or 'card'.")
            return False
    
    def report(self):
        print(f"Profit: {MoneyMachine.CURRENCY} {self.profit:.2f}")
