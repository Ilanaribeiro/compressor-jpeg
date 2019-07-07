import numpy

from itertools import chain


def zigzag_ordering(block):
    """
    Zigzag ordering in entropy coding
    """
    rows, columns = block.shape

    solution=[[] for i in range(rows+columns-1)] 
  
    for r in range(rows): 
        for c in range(columns): 
            sum = r+c 
            if(sum%2 == 0):     
                #add at beginning 
                solution[sum].insert(0,block[r][c]) 
            else:     
                #add at end of the list 
                solution[sum].append(block[r][c])

    return list(chain.from_iterable(solution))
    
 
def get_symbols(ordered_list):
    """
    Get a list of tuples of AC coefficients and number of zero before said coefficient.
    """
    zerocounter = 0
    symbols = []
    ac_list = ordered_list.copy()
    ac_list.pop(0) # Remove DC coefficient from list - first item

    for n in ac_list:
        if(n == 0):
            zerocounter += 1
        else:
            symbols.append((zerocounter, n))
            zerocounter = 0

    symbols.append((0, 0)) # EOB
    return symbols
