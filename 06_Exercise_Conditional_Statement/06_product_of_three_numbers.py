first_num = float(input())
second_num = float(input())
third_num = float(input())

if first_num == 0 or second_num == 0 or third_num == 0:
    print("zero")
else:
    count = 0
    if first_num < 0:
        count += 1

    if second_num < 0:
        count += 1

    if third_num < 0:
        count += 1

    if count % 2 != 0:
        print("negative")
    else:
        print("positive")
