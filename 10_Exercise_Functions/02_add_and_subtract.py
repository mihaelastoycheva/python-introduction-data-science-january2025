def sum_numbers(number_one: int, number_two: int) -> int:
    return number_one + number_two


def subtract(result_number: int, subtract_num: int) -> int:
    return result_number - subtract_num


def add_and_subtract(number_one: int, number_two: int, number_three: int) -> int:
    result_sum_numbers = sum_numbers(number_one, number_two)
    return subtract(result_sum_numbers, number_three)  # composition: one function calls another func


num_one = int(input())
num_two = int(input())
num_three = int(input())

result = add_and_subtract(num_one, num_two, num_three)
print(result)
