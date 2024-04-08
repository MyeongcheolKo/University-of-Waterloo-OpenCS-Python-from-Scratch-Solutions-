def romanize(x):
    s = ''
    while True:
        if x == 4 or x == 9:
            s += 'I'
            x += 1 
        elif x <= 3:
            for i in range(x):
                s += 'I'
            return s
        elif x // 5 == 1:
            s += 'V'
            x %= 5
        elif x // 10 >= 1:
            for i in range(x // 10):
                s += 'X'
            x %= 10
        
print(romanize(16))

''' 
---Alternative 1---
def romanize(num):
    dictonary = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X"]
    if num >= 0 and num <= 10:
        return dictonary[num - 1]

---Alternative 2---
def romanize(num):
    string = ""
    if(4 < num < 9):
        string = "V"
    if(num == 1 or num == 6):
        string = string + "I"
    elif(num == 2 or num == 7):
        string = string + "II"
    elif(num == 3  or num == 8):
        string = string + "III"
    elif(num == 4):
        string = "IV"
    elif(num == 9):
        string = "IX"
    elif(num == 10):
        string = "X"
    return string

'''
