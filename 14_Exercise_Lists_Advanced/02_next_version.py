software_version_string = input().split(".")
software_version_numbers = [int(num) for num in software_version_string]

software_version_numbers[-1] += 1  # add to last element +1

for num in range(len(software_version_numbers) - 1, 0, -1):

    if software_version_numbers[num] > 9:
        software_version_numbers[num] = 0
        software_version_numbers[num-1] += 1

updated_software_version = [str(num) for num in software_version_numbers]
print(".".join(updated_software_version))
