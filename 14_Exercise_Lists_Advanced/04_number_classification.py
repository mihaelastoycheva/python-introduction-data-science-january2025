def converting_int_list_into_str(int_list: list[int]) -> str:
    return ", ".join(str(num) for num in int_list)


numbers_as_string = input().split(", ")
numbers_as_int = [int(num) for num in numbers_as_string]

positive_numbers = [num for num in numbers_as_int if num >= 0]
negative_numbers = [num for num in numbers_as_int if num < 0]

even_numbers = [num for num in numbers_as_int if num % 2 == 0]
odd_numbers = [num for num in numbers_as_int if num % 2 != 0]

print(f"Positive: {converting_int_list_into_str(positive_numbers)}")
print(f"Negative: {converting_int_list_into_str(negative_numbers)}")
print(f"Even: {converting_int_list_into_str(even_numbers)}")
print(f"Odd: {converting_int_list_into_str(odd_numbers)}")
