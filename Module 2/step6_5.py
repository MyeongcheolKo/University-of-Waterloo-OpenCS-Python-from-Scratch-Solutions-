meal = 8.00
tax = 0.13 * meal
tip = int(0.15 * (meal + tax))
total = tip + tax + meal
print(total)
