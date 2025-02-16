factor = int(input())
count = int(input())
list_numbers = []

for number in range(1, count + 1):
    list_numbers.append(number * factor)

print(list_numbers)