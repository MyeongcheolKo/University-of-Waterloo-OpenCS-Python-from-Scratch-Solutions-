def total_bill(cost, age, tax):
    cost_discounted = cost
    if age >= 65:
        cost_discounted *= 0.9
    if cost < 100: 
        return cost_discounted * tax + cost_discounted + 5
    return cost_discounted * tax + cost_discounted
    
print(total_bill(99, 64, 0.2))
