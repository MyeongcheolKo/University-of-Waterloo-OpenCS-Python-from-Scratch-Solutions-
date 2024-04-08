def code_ending(s):
    str_len = len(s)
    if s[str_len - 4:str_len - 3].isspace() and s[str_len - 3:str_len - 2].isdigit() and s[str_len - 2: -1].isalpha():
        return True
    return False

def code_eight(s):
    if s[0:2].isalpha() and s[2:3].isdigit() and (s[3:4].isalpha() or s[3:4].isdigit()):
        return True
    return False
