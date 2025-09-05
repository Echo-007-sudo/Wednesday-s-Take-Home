"""
TASK: Create a ShoppingCart class.

Requirements:
1. Store cart items in a dictionary (item → quantity).
2. Provide a method to add items.
3. Provide a method to remove items.
4. Provide a method to clear the cart.
5. Provide a method to calculate total price (with price list).

Example Usage:
    prices = {"Shirt": 5000, "Shoes": 12000}
    cart = ShoppingCart(prices)
    cart.add_item("Shirt", 2)
    print(cart.calculate_total())  # 10000
    cart.remove_item("Shirt", 1)
    print(cart.calculate_total())  # 5000
"""
class ShoppingCart:
    def __init__(self):
        self.cart = {}
        #self.item = item
        #self.quantity = quantity

        #add items
        def add_item(self, item, quantity):
            item = input("Enter item: ")
            quantity = int(input("Enter quantity of item: "))
            self.cart[item] = quantity
            print(f"Added {quantity} {item}(s) to cart.")
            return
        #remove items
        def remove_item(self):
            cart.popitem(item)
            return
        #clear cart
        def clear_cart(self):
            cart.clear
            return

        #total price
        def calculate_total_price(self):
            pass




cart = ShoppingCart()

print(self.cart())
