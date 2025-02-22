ingot = input()

resources = {}

while ingot != "stop":
    quantity = int(input())

    if ingot not in resources:
        resources[ingot] = quantity
    else:
        resources[ingot] += quantity

    ingot = input()

for key, value in resources.items():
    print(f"{key} -> {value}")
