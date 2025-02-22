input_data = input()

phonebook = {}

while not input_data.isnumeric():
    persons_numbers = input_data.split("-")

    name = persons_numbers[0]
    telephone = persons_numbers[1]
    phonebook[name] = telephone

    input_data = input()

count = int(input_data)

for _ in range(count):
    name = input()

    if name in phonebook:
        for key, value in phonebook.items():
            if key == name:
                print(f"{key} -> {value}")
    else:
        print(f"Contact {name} does not exist.")
