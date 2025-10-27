class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price == other.price

    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.price < other.price

    def __str__(self):
        return f"Product(name: {self.name}, price: {self.price} руб.)"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"