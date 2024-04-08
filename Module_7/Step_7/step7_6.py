def uk_code(entry):
    """Determines if a string can be a postal code.

       Preconditions:
       entry: string of letters, digits, spaces only

       Parameters:
       entry: possible postal code

       Returns "Code" if of one of the following forms:
       "A9 9AA", "A9A 9AA", "A99 9AA", "AA9 9AA",
       "AA9A 9AA", "AA99 9AA" where 9 is any digit and
       A is any letter,
       and "Not code" otherwise
    """

    ## Return "Not code" if the length is not between 6 and 8
    if not len(entry) >= 6 and len(entry) <= 8:
        return "Not code"

    ## Return "Not code" if it does not start with a letter 
    ## or end of the form  ' 9AA'
    if not entry[0].isalpha() or not code_ending(entry):
        return "Not code"

    ## Return "Code" for valid codes of length 6
    if len(entry) == 6:
        if entry[0].isalpha() and entry[1].isdigit():
            return "Code"
    ## Return "Code" for valid codes of length 7
    elif len(entry) == 7 and entry[0].isalpha() and (entry[1].isalpha() or entry[1].isdigit()) and (entry[2].isalpha() or entry[2].isdigit()):
        return "Code"

    ## Return "Code" for valid codes of length 8
    elif code_eight(entry):
        return "Code"

    ## Return "Not code" for all other inputs
    return "Not code"
def code_ending(s):
    str_len = len(s)
    if s[str_len - 4:str_len - 3].isspace() and s[str_len - 3:str_len - 2].isdigit() and s[str_len - 2: -1].isalpha():
        return True
    return False

def code_eight(s):
    if s[0:2].isalpha() and s[2:3].isdigit() and (s[3:4].isalpha() or s[3:4].isdigit()):
        return True
    return False
