input_command = input().split()

stock = {}

total_sold_quantity = 0

while input_command[0] != "Complete":
    command = input_command[0]
    quantity = int(input_command[1])
    food = input_command[2]

    if quantity <= 0:
        continue

    if command == "Receive":
        if food not in stock:
            stock[food] = quantity
        else:
            stock[food] += quantity

    elif command == "Sell":
        if food not in stock:
            print(f"You do not have any {food}.")
            input_command = input().split()
            continue
        elif stock[food] < quantity:
            print(f"There aren't enough {food}. You sold the last {stock[food]} of them.")
            total_sold_quantity += stock[food]
            stock.pop(food)
        else:
            print(f"You sold {quantity} {food}.")
            total_sold_quantity += quantity
            stock[food] -= quantity
            if stock[food] == 0:
                stock.pop(food)

    input_command = input().split()

for key, value in stock.items():
    print(f"{key}: {value}")

print(f"All sold: {total_sold_quantity} goods")
