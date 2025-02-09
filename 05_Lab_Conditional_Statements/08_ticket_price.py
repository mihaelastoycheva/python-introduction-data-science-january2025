STUDENT_TICKET_PRICE = 1.00
REGULAR_TICKET_PRICE = 1.60

ticket = input()

if ticket == "student":
    print(f"${STUDENT_TICKET_PRICE:.2f}")
elif ticket == "regular":
    print(f"${REGULAR_TICKET_PRICE:.2f}")
else:
    print("Invalid ticket type!")

# --------------------------------

# ticket = input()
# price = ""
#
# if ticket == "student":
#     price = "$1.00"
# elif ticket == "regular":
#     price = "$1.60"
# else:
#     price = "Invalid ticket type"
# print(price)

