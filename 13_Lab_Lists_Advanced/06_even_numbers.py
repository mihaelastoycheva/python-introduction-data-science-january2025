numbers = [int(number) for number in input().split(", ")]

indexes = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(indexes)
