count_numbers = int(input())

max_num = float("-inf")  # -sys.maxsize

for _ in range(1, count_numbers + 1):
    entered_number = int(input())
    if max_num < entered_number:
        max_num = entered_number

print(max_num)
