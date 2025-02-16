def filtering_numbers(numbers: list, command: str) -> list[int]:
    numbers = [int(num) for num in numbers]
    filtered_list = []
    if command == "even":
        filtered_list = list(filter(lambda x: x % 2 == 0, numbers))

        #  2nd solution:
        #
        #  filtered_list = [number for number in numbers if number % 2 == 0]
    elif command == "odd":
        filtered_list = list(filter(lambda x: x % 2 != 0, numbers))
    elif command == "positive":
        filtered_list = list(filter(lambda x: x >= 0, numbers))
    elif command == "negative":
        filtered_list = list(filter(lambda x: x < 0, numbers))

    return filtered_list


count = int(input())
all_numbers = []

for _ in range(count):
    current_number = input()
    all_numbers.append(current_number)

entered_command = input()

print(filtering_numbers(all_numbers, entered_command))
