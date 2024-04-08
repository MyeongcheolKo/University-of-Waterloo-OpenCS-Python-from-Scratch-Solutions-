def code_ending(s):
    return s[-4].isspace() and s[-3].isdigit() and s[-2:].isalpha() 
