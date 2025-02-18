# input_words = input().split()
#
# result_words = []
#
# for word in input_words:
#     if len(word) % 2 == 0:
#         result_words.append(word)
#
# for result_word in result_words:
#     print(result_word)

# ----------------------------- 2nd solution (with List Comprehension):

# input_words = input().split()
#
# even_length_words = [word for word in input_words if len(word) % 2 == 0]
#
# print("\n".join(even_length_words))

# ----------------------------- 3rd solution (Filter with anonymous function):

input_words = input().split()

even_length_words = list(filter(lambda word: len(word) % 2 == 0, input_words))

print("\n".join(even_length_words))
