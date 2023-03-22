class ShoppingCart(object):
    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items_in_cart = {}

    def add_item(self, product, price):
        """Adauga produs in cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print(product + " added.")
        else:
            print(product + " is already in the cart")

    def remove_item(self, product):
        """Elimina produs din cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print(product + " removed.")
        else:
            print(product + " is not in the cart.")

my_cart = ShoppingCart("Eric")
my_cart.add_item("Ulei", 10)
my_cart.add_item("Ciocolata", 7)
print(my_cart.items_in_cart)

print("Pretul uleiului este: " , my_cart.items_in_cart["Ulei"])
my_cart.remove_item("Ulei")
print(my_cart.items_in_cart)
