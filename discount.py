prоmokod_list = {
    'zaga': 18,
    'ekaterina': 19,
}


class Discount:
    def __init__(self, description, discount_percent):
        self.description = description
        self.discount_percent = discount_percent

    @staticmethod
    def result_discount_product(price, discount_percent):
        res_discount_product = (price * discount_percent) / 100

        return res_discount_product