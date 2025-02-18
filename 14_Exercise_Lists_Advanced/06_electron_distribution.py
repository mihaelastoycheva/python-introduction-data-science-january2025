number_of_electrons = int(input())

n = 1

shells = []

while number_of_electrons > 0:
    max_electrons_in_shell = 2 * (n ** 2)

    electrons_to_add = min(number_of_electrons, max_electrons_in_shell)
    shells.append(electrons_to_add)

    number_of_electrons -= electrons_to_add
    n += 1

print(shells)
