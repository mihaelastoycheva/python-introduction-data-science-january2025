def sum_odd_and_even(number_as_string: str) -> str:
    odd_sum = 0
    even_sum = 0

    for num_str in number_as_string:

        if not num_str.isdigit() or num_str == "0":
            continue

        number = int(num_str)

        if number % 2 == 0:
            even_sum += number
        else:
            odd_sum += number

    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


string_number = input()

print(sum_odd_and_even(string_number))