def integer_type(x):
    if type(x) == int: 
        if x % 2 == 0:
            return "Even integer"
        return "Odd integer"
    return "Not an integer"