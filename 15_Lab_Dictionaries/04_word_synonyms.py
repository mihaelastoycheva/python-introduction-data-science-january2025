n = int(input())

synonyms = {}

for _ in range(n):
    key = input()
    value = input()

    if key not in synonyms.keys():
        synonyms[key] = [value]
    else:
        synonyms[key].append(value)

for key, value in synonyms.items():
    value_string = ", ".join(value)
    print(f"{key} - {value_string}")
