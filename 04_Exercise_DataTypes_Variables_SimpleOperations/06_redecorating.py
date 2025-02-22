protective_nylon_price_per_square_meter = 1.50
paint_price_per_liter = 14.50
paint_thinner_price_per_liter = 5.00

required_nylon_amount = int(input())
required_paint_amount = int(input())
required_thinner_quantity = int(input())
work_hours = int(input())

nylon_amount = (required_nylon_amount + 2) * protective_nylon_price_per_square_meter
paint_amount = (required_paint_amount + (required_paint_amount * 0.1)) * paint_price_per_liter
thinner_amount = required_thinner_quantity * paint_thinner_price_per_liter

total_amount_materials = nylon_amount + paint_amount + thinner_amount + 0.40

amount_craftsmen = (total_amount_materials * 0.3) * work_hours

total_amount = total_amount_materials + amount_craftsmen

print(f"{total_amount:.2f}")

