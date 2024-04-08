def yarn_size(stitches):
    """Determines yarn size given 4 inches of stitches.

       Preconditions:
       stitches: int > 0; 6 <= value <= 32
     
       Parameter:
       stitches: average number of stitches in 4 inches

       Returns: yarn size
    """
    SUPER_BULKY = 11
    BULKY_MAX = 15
    MEDIUM = 20
    LIGHT = 22
    LIGH_OR_FINE = 24
    FINE = 26
    if stitches <= SUPER_BULKY:
        return "Super bulky"
    elif stitches <= BULKY_MAX:
        return "Bulky"
    elif stitches <= MEDIUM:
        return "Medium"
    elif stitches <= LIGHT:
        return "Light"
    elif stitches <= LIGH_OR_FINE:
        return "Light or Fine"
    elif stitches <= FINE:
        return "Fine"
    else:
        return "Super fine"
