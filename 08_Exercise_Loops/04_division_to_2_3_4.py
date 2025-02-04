count_numbers = int(input())

divisible_by_2 = 0
divisible_by_3 = 0
divisible_by_4 = 0

for _ in range(1, count_numbers + 1):
    entered_number = int(input())

    if entered_number == 0:
        continue

    if entered_number % 2 == 0:
        divisible_by_2 += 1

    if entered_number % 3 == 0:
        divisible_by_3 += 1

    if entered_number % 4 == 0:
        divisible_by_4 += 1

perc_by_2 = (divisible_by_2 / count_numbers) * 100
perc_by_3 = (divisible_by_3 / count_numbers) * 100
perc_by_4 = (divisible_by_4 / count_numbers) * 100

print(f"{perc_by_2:.2f}%")
print(f"{perc_by_3:.2f}%")
print(f"{perc_by_4:.2f}%")