countries = input().split(", ")
capitals = input().split(", ")

mixed_dictionary = {key: value for key, value in zip(countries, capitals)}

for key, value in mixed_dictionary.items():
    print(f"{key} -> {value}")
