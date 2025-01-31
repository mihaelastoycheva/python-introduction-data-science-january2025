#       Read input:

# side_a = input()

#       When we enter for example 3, it will be string "3"
#       Input() always takes string

# --------------------------------------

# number = int(5.14)
# print(number)    --> 5

# number = float(5.14)
# print(number)    --> 5.14

# number = str(5.14)
# print(number)     --> 5

# --------------------------------------

#       Read int input:
side_a = int(input())

#       Read other data types input"
# side_a = float(input())
# side_a = str(input())

side_b = int(input())

area = side_a * side_b

print(area)

# --------------------------------------

#       Check for the data type with type()

# print(type(3.14))      --> <class 'float'>

# --------------------------------------

# print(60/8)      --> 7.5

#       Целочислено деление:
# print(60//8)      --> 7

#       Модулно деление (връща остатъка):
# print(60%8)      --> 4 (8 * 7 = 56; за да се допълни 56 до 60, трябва да добавим 4 (остатъка))
