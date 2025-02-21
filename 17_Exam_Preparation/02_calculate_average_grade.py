count = int(input())

total_sum = 0

for _ in range(count):
    grade = float(input())
    total_sum += grade

average = total_sum / count

print(f"{average:.2f}")