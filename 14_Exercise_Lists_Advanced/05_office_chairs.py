number_of_rooms = int(input())

chairs_left = 0
chairs_needed = 0

for room_number in range(1, number_of_rooms + 1):
    current_room = input().split()

    chairs_count = len(current_room[0])
    visitors_count = int(current_room[1])

    # chairs_in_the_room, number_of_visitors = current_room.split()

    difference = chairs_count - visitors_count

    if difference > 0:
        chairs_left += difference

    elif difference < 0:
        print(f"{abs(difference)} more chairs needed in room {room_number}")
        chairs_needed += abs(difference)


if chairs_needed == 0:
    print(f"Game On, {chairs_left} free chairs left")


