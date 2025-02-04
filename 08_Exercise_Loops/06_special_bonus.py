stop_number = int(input())
entered_number = int(input())

last_number = 0

while entered_number != stop_number:
    last_number = entered_number
    entered_number = int(input())

result = last_number + (last_number * 0.2)
print(int(result))
