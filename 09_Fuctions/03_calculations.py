def calculate(operator: str, first_number: int, second_number: int) -> int:
    result = 0
    if operator == "multiply":
        result = first_number * second_number
    elif operator == "divide":
        result = first_number //  second_number
    elif operator == "add":
        result = first_number + second_number
    elif operator == "subtract":
        result = first_number - second_number
    return result


operator = input()
first_number = int(input())
second_numbers = int(input())

print(calculate(operator, first_number, second_numbers))
