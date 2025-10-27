class Order:
    def __init__(self, products):
        self.products = products

    def __str__(self):
        return f"Order(products: {self.products})"

    def __repr__(self):
        return f"Order({repr(self.products)})"