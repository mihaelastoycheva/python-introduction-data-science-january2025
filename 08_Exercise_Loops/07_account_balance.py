command = input()

balance = 0

while command != "End":
    money = float(command)  # casting to number(float)

    if money > 0:
        print(f"Increase: {money:.2f}")
    elif money < 0:
        print(f"Decrease: {abs(money):.2f}")

    balance += money
    command = input()

print(f"Balance: {balance:.2f}")
