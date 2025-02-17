wagons = int(input())
train = []

# for _ in range(wagons):
#     train.append(0)

train = [0] * wagons

command = input()

while command != "End":
    command = command.split()
    action = command[0]

    if action == "add":
        people = int(command[1])
        train[-1] += people

    elif action == "insert":
        index, people = int(command[1]), int(command[2])
        train[index] += people

    elif action == "leave":
        index, people = int(command[1]), int(command[2])
        train[index] -= people

    command = input()

print(train)