class Customer:
    def __init__(self, name, orders):
        self.name = name
        self.orders = orders

    def __str__(self):
        return f"Customer(name: {self.name}, orders: {self.orders})"

    def __repr__(self):
        return f"Customer('{self.name}', {self.orders})"