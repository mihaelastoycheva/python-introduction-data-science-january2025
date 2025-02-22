input_chars_as_list = list(input())

count = len(input_chars_as_list) - 1
index = 0

while count >= 0:
    if input_chars_as_list[index] == " ":
        input_chars_as_list.pop(index)
        count -= 1

    index += 1
    count -= 1

characters_count = {}

for char in input_chars_as_list:
    characters_count[char] = input_chars_as_list.count(char)

for key, value in characters_count.items():
    print(f"{key} -> {value}")
