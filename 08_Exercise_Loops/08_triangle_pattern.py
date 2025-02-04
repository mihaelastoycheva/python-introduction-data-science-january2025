# work = input()
#
# for row in range(1, len(work) + 1):
#     for col in range(row):
#         print(work[col], end=" ")
#     print()
#
# ------------------------------------

work = input()

row = 1

while row <= len(work):
    col = 0

    while col < row:
        print(work[col], end=" ")
        col += 1
    print()
    row += 1
