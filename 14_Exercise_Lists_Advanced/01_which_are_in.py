# substrings = input().split(", ")
#
# words = input().split(", ")
#
# result_list = []
#
# for substring in substrings:
#     for word in words:
#         if substring in word and substring not in result_list:
#             result_list.append(substring)
#
# print(result_list)

# -----------

substrings = input().split(", ")

words = input().split(", ")

result_list = []

for substring in substrings:
    for word in words:
        if substring in word:
            result_list.append(substring)
            break

print(result_list)
