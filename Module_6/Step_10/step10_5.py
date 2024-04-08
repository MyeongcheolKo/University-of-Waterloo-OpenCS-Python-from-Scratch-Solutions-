def is_multiple(number, factor):
    return number % factor == 0

def leap_year(num):
    if is_multiple(num, 4) and is_multiple(num,100) and is_multiple(num,400) \
        or (is_multiple(num,4) and not is_multiple(num,100)):
        return "Leap year"
    return "Common year"
