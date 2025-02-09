def create_absolute_values(list_with_numbers: list) -> list:
    final_list = []
    for current_number in list_with_numbers:
        final_list.append(abs(current_number))
    return final_list


numbers_as_string = input().split()

numbers_as_digits = []

for number in numbers_as_string:
    numbers_as_digits.append(float(number))

print(create_absolute_values(numbers_as_digits))
