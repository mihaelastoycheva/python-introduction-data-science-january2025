list_numbers = input().split()
count = int(input())

numbers = [int(num) for num in list_numbers]

for _ in range(count):
    min_number = min(numbers)
    numbers.remove(min_number)

numbers = ", ".join(str(num) for num in numbers)
print(numbers)
