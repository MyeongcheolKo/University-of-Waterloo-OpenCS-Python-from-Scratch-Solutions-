def off_peak(data):
    if type(data) == int and data >= 0 and data < 24:
        if data < 9 or data > 17:
            return "Off peak"
        return "Peak"
    return "Not a time"
