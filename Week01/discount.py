# You work for a retail store that wants to increase sales on Tuesday and Wednesday, which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.

from datetime import datetime

subTotal = 1

while subTotal > 0:
    subTotal = float(input('\nPlease enter subtotal: '))

    date = datetime.now()
    day = date.weekday()
    discount = 0
    originalPrice = 0
    short = 0

    if (day == 1 or day == 2) and subTotal >= 50:
        originalPrice = subTotal
        discount = subTotal * 0.10
        subTotal -= discount
    elif (day == 1 or day == 2) and subTotal < 50:
        short += 50 - subTotal

    tax = subTotal * 0.06
    total = subTotal + tax


    print(f"\nSubtotal: {subTotal:.2f}") if originalPrice == 0 else print(f"\nSubtotal: {originalPrice}")
    if discount > 0:
        print(f"Discount: -{discount:.2f}")
    elif short > 0:
        print(f"You need to spend ${short:.2f} more to receive a 10% discount.")
    print(f"Sales Tax: {tax:.2f}")
    print(f"TOTAL: {total:.2f}\n")

