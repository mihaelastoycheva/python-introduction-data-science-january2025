first_seconds = int(input())
sec_seconds = int(input())
third_seconds = int(input())

sum_seconds = first_seconds + sec_seconds + third_seconds

minutes = 0

if sum_seconds / 60 > 0:
    minutes = int(sum_seconds / 60)

seconds = sum_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
