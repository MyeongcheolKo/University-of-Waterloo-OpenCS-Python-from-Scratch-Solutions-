def is_time(x, y):
    if x >= 0 and x <= 23 and y >= 0 and y <= 59:
        return "Passes"
    return "Fails"