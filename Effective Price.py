units_sold = 8000
units_returned = 10000 - units_sold
discount = 0.06
retailer_display_cost = 100000
normal_price = 150

if units_sold >= 10000:
    effective_price = (1 - discount) * normal_price
else:
    effective_price = normal_price

effective_price += retailer_display_cost / units_sold

print("The effective price of the product is:", effective_price)
