from discount import (
    Discount,
    prоmokod_list
)
from product import Product
from customer import Customer
from order import Order


discount_magazin = {
    1: Discount("Сезонная скидка", 15),
    2: Discount("Промокод", "Введите промокод для получения скидки"),
}

product_magazin = {
    1: Product("Поршень - Камаз", 1500),
    2: Product("Задняя Фара (Прав) - Камаз", 500),
    3: Product("Цилиндр - Камаз", 1700),
    4: Product("Передняя Фара (Лев) - Камаз", 510),
}

customer_magazin = {
    # 1: Customer(None, None),
}

order_magazin = {
    # 1: Order([None]),
}


def main():
    print(
        f"{'-' * 70}\n"
        f"|{' ' * 25} Каталог товаров {' ' * 25} |\n"
        f"{'-' * 70}\n"
    )

    print(f"{' ' * 1} ID {' ' * 3} Наименование {' ' * 5} Цена")
    for i, product in product_magazin.items():
        print(f"[ {i} ][ {product.name} ][ {product.price} руб. ]")

    user_num_order_product = input(
        "\n[+] Введите [ ID ] товаров которые хотите заказать (пример: 1 2 3 ...)--> ... "
    ).replace(' ', '')

    user_name_input = input("Введите ваше имя (это для оформления заказа) --> ... ")

    if len(order_magazin) > 0:
        index_order = int(max(order_magazin.keys()) + 1)
        order_magazin[index_order] = Order(user_num_order_product)
        if len(customer_magazin) > 0:
            customer_magazin[int(max(customer_magazin.keys()) + 1)] = Customer(user_name_input, index_order)
        else:
            customer_magazin[1] = Customer(user_name_input, index_order)
    else:
        order_magazin[1] = Order(user_num_order_product)

    def order_print():
        result_sym_order = 0
        for index, orders in order_magazin.items():
            for char in orders.products:
                key = int(char)
                if key in product_magazin:
                    product_in_order = product_magazin[key]
                    result_sym_order += product_in_order.price

        print(f"\n[+] У вас в корзине следующие товары на СУММУ: [ {result_sym_order} руб. ]")
        for index, orders in order_magazin.items():
            for char in orders.products:
                key = int(char)
                if key in product_magazin:
                    product_in_order = product_magazin[key]
                    print(f"\t[ {key} ] Товар: [ {product_in_order.name} ] Цена: [ {product_in_order.price} руб. ]")

        return result_sym_order

    def making_an_order():
        print(
            f"{'-' * 70}\n"
            f"|{' ' * 24} Оформление заказа {' ' * 24} |\n"
            f"{'-' * 70}\n"
        )

        usr_input_res = \
            f"[+] Выберите скидку:\n\n" \
            f"\t[ 1 ] {discount_magazin[1].description} - {discount_magazin[1].discount_percent}%\n" \
            f"\t[ 2 ] {discount_magazin[2].description} ---[ для получения скидки нужно ввести промокод ]\n\n" \
            f"[+] Введите цифру --> ... "

        user_input_result = int(input(usr_input_res))

        if user_input_result == 2:
            usr_input_promokod = input("\n[+] Введите промокод: ")

            if usr_input_promokod in prоmokod_list.keys():
                discount_magazin[2].discount_percent = prоmokod_list[usr_input_promokod]
                """
                   Вычисление для промокода
                """

                total_order_sum = order_print()
                print(
                    f"Промокод [ {usr_input_promokod} ] даёт {discount_magazin[2].discount_percent}% скидки к общей суммы.\n"
                    f"У вас заказы на сумму [ {total_order_sum} руб. ] и скидка [ {discount_magazin[2].discount_percent}% ]\n"
                    f"[+] Итого к оплате: "
                    f"[ {discount_magazin[2].result_discount_product(total_order_sum, discount_magazin[2].discount_percent)} руб. ]"
                )

            else:
                print("\n[-] В базе нет такого промокода, попробуйте ввести другой :(\n")

                main()
        else:
            print(
                f"\n[+] Выбрана скидка: "
                f"{discount_magazin[user_input_result].description} - "
                f"{discount_magazin[user_input_result].discount_percent}%\n"
            )
            """
                Вычисление для скидки
            """
            total_order_sum = order_print()

            print(
                f"У вас заказы на сумму [ {total_order_sum} руб. ] и скидка [ {discount_magazin[1].discount_percent}% ]\n"
                f"[+] Итого к оплате: "
                f"[ {discount_magazin[1].result_discount_product(total_order_sum, discount_magazin[1].discount_percent)} руб. ]"
            )

    making_an_order()

if __name__ == '__main__':
    main()