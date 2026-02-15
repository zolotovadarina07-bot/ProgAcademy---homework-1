fuel_price_per_liter = 1.2
consumption_per_hundred_km = 8
distance = 120
liter_needed = (distance / 100) * consumption_per_hundred_km
total = liter_needed * fuel_price_per_liter
print('Your total cost is :', total)