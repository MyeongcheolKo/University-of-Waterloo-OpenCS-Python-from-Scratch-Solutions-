DOZEN = 12         # number of items in a dozen
BAKERS_DOZEN = 13  # number of items in a baker's dozen
DOZEN_COST = 10    # cost of a dozen
SINGLE_COST = 1    # cost of a single item

def bakers(items):
    """Determines cost of items with baker's dozen discount.

       Preconditions:
       items: int > 0

       Parameters:
       items: number of items 
   
       Returns: total cost with discount of 13 for the cost of a dozen
    """   
    total = 0
    total += items // BAKERS_DOZEN * DOZEN_COST 
    items %= BAKERS_DOZEN
    
    if items == 12:
        total += DOZEN_COST 
    else:
        total += items * SINGLE_COST
    return total
