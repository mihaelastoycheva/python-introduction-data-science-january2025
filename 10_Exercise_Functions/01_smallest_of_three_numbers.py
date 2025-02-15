def smallest_numbers(num_one: int, num_two: int, num_three: int) -> int:
    return min(num_one, num_two, num_three)


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(smallest_numbers(number_one, number_two, number_three))
