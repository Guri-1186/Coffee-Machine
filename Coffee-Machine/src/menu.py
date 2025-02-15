import json
from pathlib import Path

base_dir = Path(".")
json_file = base_dir / "data" / "coffee_shop_data.json"
class Menu:
    def __init__(self, json_file):
        self.json_file = json_file
        self._menu_data = self.load_menu_data()

    def load_menu_data(self):
        try:
            with self.json_file.open("r") as file:
                return json.load(file)["MENU"]
        except FileNotFoundError:
            print("Error: Menu file not found.")
            return {}
        except json.JSONDecodeError:
            print("Error: Menu file contains invalid JSON.")
            return {}
        except Exception as e:
            print(f"Unexpected error while loading menu data: {e}")
            return {}

    @property
    def menu_items(self):
        return list(self._menu_data.keys())

    def get_drink_details(self, drink_name):
        return self._menu_data.get(drink_name, None)
    