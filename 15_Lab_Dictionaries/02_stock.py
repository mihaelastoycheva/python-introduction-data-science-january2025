items = input().split()
searched_products = input().split()
available_products = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    available_products[key] = value

for searched_product in searched_products:
    if searched_product in available_products.keys():
        print(f"We have {available_products[searched_product]} of {searched_product} left")
        continue

    print(f"Sorry, we don't have {searched_product}")
