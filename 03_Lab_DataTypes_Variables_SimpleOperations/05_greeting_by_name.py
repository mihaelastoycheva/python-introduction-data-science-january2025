name = str(input())
print("Hello, " + name + "!")

#       Concatenate ONLY strings (str + int is not allowed)
#
# name = 5
# print("Hello " + name + "!")      --> Error
#
#
#       Solution (transform from num to str):
#
# name = 5
# print("Hello " + str(name) + "!")      --> Hello 5!
#
# --------------------------------------
#
#       Formatting with f-string / placeholders {}:
#
# print(f"Hello, {name}!")      --> it'll work the same with nums
# print(f"Hello, {name:.2f}!")  --> format num after floating point (5.00)
#
# --------------------------------------
#
#       Calculate dozens, hundreds, thousands...:
#
# print(3456%10)      --> returns dozens (6) / the last num
# print(3456%100)      --> returns hundreds and dozens (56) / last 2 nums (two zeros)
