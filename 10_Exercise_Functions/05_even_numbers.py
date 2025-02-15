def is_even(numbers_as_string: list[str]) -> list:
    # iterating through the whole list and casting each element to int; So-called List Comprehension:
    numbers = [int(num) for num in numbers_as_string]

    return list(filter(lambda x: x % 2 == 0, numbers))


string_numbers = input().split()  # by default, it is separated with spaces
even_number = is_even(string_numbers)
print(even_number)
