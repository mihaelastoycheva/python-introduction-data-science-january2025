number_chicken_menus = int(input())
number_fish_menus = int(input())
number_vegetarian_menus = int(input())

price_chicken_menus = number_chicken_menus * 10.35
price_fish_menus = number_fish_menus * 12.40
price_vegetarian_menus = number_vegetarian_menus * 8.15

cost_menus = price_chicken_menus + price_fish_menus + price_vegetarian_menus

price_dessert = cost_menus * 0.2

total_order_price = cost_menus + price_dessert + 2.50

print(f"{total_order_price}")
