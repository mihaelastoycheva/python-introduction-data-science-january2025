price_training_per_year = int(input())

price_sneakers = price_training_per_year - (price_training_per_year * 0.4)
price_per_team = price_sneakers - (price_sneakers * 0.2)
price_basketball = (1 / 4) * price_per_team
price_accessories = (1 / 5) * price_basketball

total_price = price_training_per_year + price_sneakers + price_per_team + price_basketball + price_accessories

print(f"{total_price}")
