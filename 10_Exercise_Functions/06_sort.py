def sort_numbers(numbers_as_string: list[str]) -> list[int]:
    numbers = [int(num) for num in numbers_as_string]
    return sorted(numbers)  # Sorting in ascending order

    # return sorted(numbers, reverse=True)  Sorting in descending order


string_numbers = input().split()
sorted_numbers = sort_numbers(string_numbers)

print(sorted_numbers)
