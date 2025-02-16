numbers_as_string = input().split()

numbers = [int(num) for num in numbers_as_string]

even_sum = sum(num for num in numbers if num % 2 == 0)
print(even_sum)
