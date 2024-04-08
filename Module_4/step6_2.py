def target(age, rest_rate, intensity):
    max_rate = 220 - age
    reserve = max_rate - rest_rate
    return rest_rate + intensity * reserve
