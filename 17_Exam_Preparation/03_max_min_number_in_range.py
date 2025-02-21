input_numbers = [int(num) for num in input().split()]

start_index = int(input())
end_index = int(input())

second_list = []

for index in range(start_index, end_index + 1):
    second_list.append(input_numbers[index])

min_number = min(second_list)
max_number = max(second_list)

sum_of_min_max = min_number + max_number

print(sum_of_min_max)