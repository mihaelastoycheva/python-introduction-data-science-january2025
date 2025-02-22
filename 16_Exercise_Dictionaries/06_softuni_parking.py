count = int(input())

parking_system = {}

for _ in range(count):
    commands = input().split()

    command = commands[0]
    username = commands[1]

    if command == "register":
        license_plate_number = commands[2]
        if username in parking_system:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_system[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif command == "unregister":
        if username not in parking_system:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_system[username]

for key, value in parking_system.items():
    print(f"{key} => {value}")
