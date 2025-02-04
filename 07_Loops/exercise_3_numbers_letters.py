number_of_letter = int(input())

for first_symbol in range(97, 97 + number_of_letter):
    for second_symbol in range(97, 97 + number_of_letter):
        for third_symbol in range(97, 97 + number_of_letter):
            print(f"{chr(first_symbol)}{chr(second_symbol)}{chr(third_symbol)}")

# formatting chars -> chr(variable)
