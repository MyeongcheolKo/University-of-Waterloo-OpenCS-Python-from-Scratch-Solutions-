def total_bill(cost, age, tax):
    if age >= 65:
        cost = cost * 0.9
    return cost + cost * tax