number = int(input())

temp = number
is_special = True

while temp > 0:
    digit = temp % 10 #212 % 10 == 2 -> 21 % 10 == 1

    if number % digit != 0:
        is_special = False
        break

    temp //= 10  # 212 // 10 = 21 -> 21 // 10 = 2 -> 0

if is_special:
    print(f"{number} is special")
else:
    print(f"{number} is not special")
