numbers_string = input().split(", ")
beggars_count = int(input())

numbers = [int(num) for num in numbers_string]

beggars_sums = []

for beggar in range(beggars_count):
    current_sum = 0

    for num in range(beggar, len(numbers), beggars_count):
        current_sum += numbers[num]

    beggars_sums.append(current_sum)

print(beggars_sums)
