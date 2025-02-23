season = input()
accommodation_type = input()
count_days = int(input())

price_per_night = 0
discount = 0

if season == "Spring":
    discount = 0.2
    if accommodation_type == "Hotel":
        price_per_night = 30
    elif accommodation_type == "Camping":
        price_per_night = 10

elif season == "Summer":
    if accommodation_type == "Hotel":
        price_per_night = 50
    elif accommodation_type == "Camping":
        price_per_night = 30

elif season == "Autumn":
    discount = 0.3
    if accommodation_type == "Hotel":
        price_per_night = 20
    elif accommodation_type == "Camping":
        price_per_night = 15

elif season == "Winter":
    discount = 0.1
    if accommodation_type == "Hotel":
        price_per_night = 40
    elif accommodation_type == "Camping":
        price_per_night = 10

expenses = count_days * price_per_night

if discount != 0:
    total_expenses_with_discount = expenses - (expenses * discount)
    print(f"{total_expenses_with_discount:.2f}")
else:
    print(f"{expenses:.2f}")
