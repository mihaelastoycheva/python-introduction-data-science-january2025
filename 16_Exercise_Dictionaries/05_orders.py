input_data = input()

orders_dictionary = {}

while input_data != "buy":
    orders_list = input_data.split()

    product = orders_list[0]
    price = float(orders_list[1])
    quantity = int(orders_list[2])

    if product not in orders_dictionary:
        orders_dictionary[product] = [price, quantity]
    else:
        for key, value in orders_dictionary.items():
            if key == product:
                value[0] = price
                value[1] += quantity

    input_data = input()

for key, value in orders_dictionary.items():

    print(f"{key} -> {(value[0] * value[1]):.2f}")
