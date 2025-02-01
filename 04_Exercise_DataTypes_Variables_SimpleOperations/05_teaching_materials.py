PRICE_PACKAGE_PENS = 5.80
PRICE_PACKAGE_MARKERS = 7.20
PRICE_BOARD_CLEANER = 1.20

number_packages_pens = int(input())
number_packages_markers = int(input())
liter_of_board_cleaner = int(input())
discount = int(input()) / 100

sum_without_discount = ((number_packages_pens * PRICE_PACKAGE_PENS)
                        + (number_packages_markers * PRICE_PACKAGE_MARKERS)
                        + (liter_of_board_cleaner * PRICE_BOARD_CLEANER))

total_sum = sum_without_discount - (sum_without_discount * discount)

print(total_sum)
