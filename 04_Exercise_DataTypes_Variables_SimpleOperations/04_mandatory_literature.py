pages_book = int(input())
pages_per_hour = int(input())
days = int(input())

needed_time = pages_book // pages_per_hour
needed_time_per_day = needed_time / days

print(needed_time_per_day)