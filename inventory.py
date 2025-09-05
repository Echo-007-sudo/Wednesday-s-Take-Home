"""
TASK: Create an Inventory class.

Requirements:
1. Store items in a dictionary (item_name → quantity).
2. Provide a method to add items (with quantity).
3. Provide a method to remove items (only if available).
4. Provide a method to update stock levels.
5. Provide a method to display all inventory items.

Example Usage:
    treasure_store = Inventory()
    favour_store = Inventory()

    treasure_store.add_item("Apples", 50)
    treasure_store.add_item("Bananas", 30)
    treasure_store.remove_item("Apples", 10)
    print(treasure_store.show_inventory())  # {"Apples": 40, "Bananas": 30}

    favour_store.add_item("Milk", 50)
    favour_store.add_item("Garri", 30)
    favour_store.remove_item("Milk", 40)
    print(treasure_store.show_inventory())  # {"Milk": 10, "Garri": 30}
"""

class Inventory:
    def __init__(self):
        self.store = {}

    def add_item(self, item, quantity):
        if item in self.store:
            self.store[item] += quantity
        else:
            self.store[item] = quantity

    def remove_item(self, item, quantity):
        if item in self.store:
            if self.store[item] >= quantity:
                self.store[item] -= quantity
                if self.store[item] == 0:
                    del self.store[item]
            else:
                return f"Not enough {item} in stock"
        else:
            return f"Item not available in store"

    def update_stock_levels(self, item, quantity):
        if item in self.store:
            self.store[item] = quantity
        else:
            return f"Item not available in store"

    def display_inventory(self):
        print("Current Inventory:")
        for item, quantity in self.store.items():
            print(f"{item}: {quantity}")

treasure_store = Inventory()
favour_store = Inventory()

treasure_store.add_item("Apple", 50)
treasure_store.add_item("Banana", 30)
treasure_store.remove_item("Apple", 10)
favour_store.add_item("Milk", 50)
favour_store.add_item("Garri", 30)
favour_store.remove_item("Milk", 40)

print("===>Treasure Store Inventory:")
treasure_store.display_inventory()
print()
print("===>Favour Store Inventory:")
favour_store.display_inventory()

