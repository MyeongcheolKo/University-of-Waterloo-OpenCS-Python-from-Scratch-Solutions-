def upper_lower(plain):
    mid = len(plain) // 2
    if len(plain) % 2 != 0:
        mid += 1
    first_half = plain[:mid].upper()
    second_half = plain[mid:].lower()
    return first_half + second_half
    
print(upper_lower("string"))
