"""
TASK: Create a RestaurantOrder class.

Requirements:
1. Store orders in a dictionary (item → quantity).
2. Provide a method to add items to the order.
3. Provide a method to remove items from the order.
4. Provide a method to calculate the total bill (use a price list dictionary).
5. Provide a method to show the current order.

Example Usage:
    prices = {"Pizza": 2000, "Burger": 1500, "Drink": 500}
    order = RestaurantOrder(prices)
    order.add_item("Pizza", 2)
    order.add_item("Drink", 3)
    print(order.calculate_total())  # 5500
"""

class RestaurantOrder:
    def __init__(self):
        self.orders = {}

    def add_order(self, item, quantity, price):
        if item in self.orders:
            print("Your order has been captured already. Do you want to update the quantity?")
            self.orders[item]["quantity"] += quantity
        else:
            self.orders[item] = {"quantity": quantity, "price": price}

    def remove_items(self, item):
        if item in self.orders:
            del self.orders[item]
        else:
            print("Item not in orders.")

    def calculate_total_bill(self):
        total = 0
        for item, details in self.orders.items():
            total += details["quantity"] * details["price"]
        return total

    def display_current_order(self):
        print("Current Order:")
        for item, details in self.orders.items():
            print(f"{item}: {details['quantity']} , N{details['price']:.2f} = N{details['quantity'] * details['price']:.2f}")
        print(f"Total Bill: N{self.calculate_total_bill():.2f}")

order = RestaurantOrder()
order.add_order("Pizza", 2, 2000)
order.add_order("Drink", 3, 500)
order.display_current_order()


