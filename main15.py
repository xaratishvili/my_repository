class ShoppingCart:
    def __init__(self):
        self.products = {}

    def add_product(self, product, price):
        if product not in self.products:
            self.products[product] = price

    def remove_product(self, product):
        if product in self.products:
            del self.products[product]

    def calculate_total(self):
        total_price = sum(self.products.values())
        return total_price

    def display_cart(self):
        print("კალათაშია: ")
        for product, price in self.products.items():
            print(f"{product}: {price} ლარი")


cart = ShoppingCart()

cart.add_product("პური", 1)
cart.add_product("კარაქი", 12)
cart.add_product("წყალი", 3)
cart.add_product("ზეთი", 5)


cart.remove_product("ზეთი")
cart.remove_product("კარაქი")


total_price = cart.calculate_total()
cart.display_cart()
print(f"სულ თანხა: {total_price} ლარი")


