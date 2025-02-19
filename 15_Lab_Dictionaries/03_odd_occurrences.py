input_elements = [word.lower() for word in input().split()]

count_words = {}

for element in input_elements:
    count_words[element] = input_elements.count(element)

for key, value in count_words.items():
    if value % 2 != 0:
        print(key, end=" ")
