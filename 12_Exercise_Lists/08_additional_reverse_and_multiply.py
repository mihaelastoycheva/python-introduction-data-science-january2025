# Input:
numbers_as_string = input().split()
multiplier = int(input())

# Cast string list to int list:
numbers = [int(num) for num in numbers_as_string]

# Reverse list
reversed_list = list(reversed(numbers))

# Generate new list with multiplied elements
result_list = []
for num in reversed_list:
    result_list.append(num * multiplier)

# Output:
print(result_list)
