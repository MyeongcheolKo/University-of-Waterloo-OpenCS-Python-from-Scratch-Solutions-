s = input("Enter a string: ")
while(len(s) < 2):
    s = input("length has to be at least 2: ")

half = len(s) // 2
print(s[:half].upper() + s[half:].lower())
