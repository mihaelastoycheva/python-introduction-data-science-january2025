end = int(input())
sum = 0
final_string = ""

for i in range(1, end + 1):
    sum += i
    if i == end:
        final_string += f"{i}="
    else:
        final_string += f"{i}+"

final_string += f"{sum}"
print(final_string)
