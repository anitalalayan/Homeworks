def total_price(*items, tax_rate = 0.05 ):
    subtotal = 0.0
    for price in items:
        subtotal += price

    tax_amount = subtotal * tax_rate
    total_price = tax_amount + subtotal

    return total_price


items = [25.99, 14.50, 8.75, 9.99, 12.25, 17.50, 6.99, 21.45, 5.75, 30.00]

print(f" Total price including tax: £{total_price(*items)}")
