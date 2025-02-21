dollar_in_leva = 1.57  # leva

cpu_price_dollars = float(input())
video_card_price_dollars = float(input())
ram_price_dollars = float(input())
ram_count = int(input())
percent_discount = float(input())

cpu_price_leva = cpu_price_dollars * dollar_in_leva
video_card_price_leva = video_card_price_dollars * dollar_in_leva
ram_price_leva = ram_price_dollars * dollar_in_leva

total_ram_price = ram_price_leva * ram_count

cpu_price_discount = cpu_price_leva - (cpu_price_leva * percent_discount)
video_card_price_discount = video_card_price_leva - (video_card_price_leva * percent_discount)

total_sum = cpu_price_discount + video_card_price_discount + total_ram_price

print(f"Money needed - {total_sum:.2f} leva.")
