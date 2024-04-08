age = 35
rest_heart = 65
intensity = .7
max_heart = 220 - age
reserve = max_heart - rest_heart
target = rest_heart + intensity * reserve
print(target)
