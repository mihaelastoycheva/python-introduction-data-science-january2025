list_numbers = input().split()

opposite_numbers = []

for number in list_numbers:
    num = -int(number)
    opposite_numbers.append(num)

print(opposite_numbers)