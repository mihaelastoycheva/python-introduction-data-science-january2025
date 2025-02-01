deposit_amount = float(input())
term_of_deposit = int(input())
annual_interest_rate = float(input()) / 100

amount = deposit_amount + term_of_deposit * (deposit_amount * annual_interest_rate) / 12

print(amount)
