numbers_as_string = input().split(", ")
numbers_as_int = [int(num) for num in numbers_as_string]

group = 10

while numbers_as_int:
    current_values_in_group = [num for num in numbers_as_int if num <= group]
    # keeps only the values in the current group

    print(f"Group of {group}'s: {current_values_in_group}")

    numbers_as_int = [num for num in numbers_as_int if num > group]
    # keeps only the values that had left after the grouping

    group += 10
