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
                solution[sum].insert(0,matrix[r][c]) 
            else:     
                #add at end of the list 
                solution[sum].append(matrix[r][c])

    return list(chain.from_iterable(solution))
    

matrix = numpy.arange(64).reshape((8,8))
ordered_list = zigzag_ordering(matrix)

print(matrix)
print(ol)