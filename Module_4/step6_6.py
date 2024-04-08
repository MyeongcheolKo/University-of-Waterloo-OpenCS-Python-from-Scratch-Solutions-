def meal_bill(cost, tip, tax):
    tax = tax / 100 
    tip = tip / 100
    total = cost + tip * cost + tax * cost
    return total
    
print(meal_bill(100, 15, 13)) 
