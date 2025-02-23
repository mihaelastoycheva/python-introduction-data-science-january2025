first_num = input()
second_num = input()
operator = input()

if operator == "+":
    print(f"{first_num} + {second_num} = {(float(first_num) + float(second_num)):.2f}")
elif operator == "-":
    print(f"{first_num} - {second_num} = {(float(first_num) - float(second_num)):.2f}")
elif operator == "*":
    print(f"{first_num} * {second_num} = {(float(first_num) * float(second_num)):.2f}")
elif operator == "/":
    print(f"{first_num} / {second_num} = {(float(first_num) / float(second_num)):.2f}")
