square_meters = float(input())

cost_of_landscaping = square_meters * 7.61

price_with_discount = cost_of_landscaping * 0.18

final_price = cost_of_landscaping - price_with_discount

print(f"The final price is: {final_price} lv.\n" 
      f"The discount is: {price_with_discount} lv.")
