s = input("Enter a string of length a least 2: ")
while (len(s) < 2):
    s = input("Enter a string of length a least 2: ")

print(s[-1] + s[1:-1] + s[0])
