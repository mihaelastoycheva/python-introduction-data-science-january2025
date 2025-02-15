def min_max_sum(numbers_as_string: list[str]) -> tuple[int, int, int]:
    numbers = [int(num) for num in numbers_as_string]
    return min(numbers), max(numbers), sum(numbers)


string_numbers = input().split()
min_number, max_number, sum_numbers = min_max_sum(string_numbers)

print(f"The minimum number is {min_number}\n"
      f"The maximum number is {max_number}\n"
      f"The sum number is: {sum_numbers}")
