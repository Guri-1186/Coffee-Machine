import hashlib
class Admin:
    def __init__(self, password):
         self._hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    def validate_password(self):
        user_input = input("Please enter the admin password: ").strip()
        return hashlib.sha256(user_input.encode()).hexdigest() == self._hashed_password
    
    def refill_resources(self, coffee_machine):
        try:
            coffee_machine.resources["water"] += int(input("Enter new water amount (ml): "))
            coffee_machine.resources["milk"] += int(input("Enter new milk amount (ml): "))
            coffee_machine.resources["coffee"] += int(input("Enter new coffee amount (g): "))
            print("Resources successfully refilled!")
        except ValueError:
            print("Invalid input. Please enter numbers only.")