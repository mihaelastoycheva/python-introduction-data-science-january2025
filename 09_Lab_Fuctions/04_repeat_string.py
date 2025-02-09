def repeating_string(current_string, current_counter) -> str:
    result = ""
    for _ in range(current_counter):
        result += current_string
    return result


string = input()
counter = int(input())

print(repeating_string(string, counter))

# ---------------------

# 2nd variation

# print(string * counter)

# ---------------------

# 3rd variation with lambda function

# final_string = lambda some_string, some_counter: some_string * some_counter
# print(final_string(string, counter))

# ---------------------

# Twodimensional list, sorting with lambda

# x = [
#     [1, 18, 2],
#     [2, 9, 4],
#     [3, 1, 1]
# ]
#
# x = sorted(x, key=lambda x: x[2])  # sorting by the last element in the lists
# print(x)
