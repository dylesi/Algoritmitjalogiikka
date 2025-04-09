from listFunctions import *

def quicksort(numlist):
    
    pivotcounter = 0
    numcounter = 0
    
    while numcounter != numlist[len(numlist) - 1 - pivotcounter]:
        print(numlist)
        if numlist[0 + numcounter] > numlist[len(numlist) - 1 - pivotcounter]:
            
            numlist[0 + numcounter], numlist[len(numlist) - 1 - pivotcounter] = numlist[len(numlist) - 1 - pivotcounter], numlist[0 + numcounter]
            if numlist[len(numlist) - 2 - pivotcounter] >= numlist[len(numlist) - 1 - pivotcounter]:
                numlist[len(numlist) - 2 - pivotcounter], numlist[len(numlist) - 1 - pivotcounter] = numlist[len(numlist) - 1 - pivotcounter], numlist[len(numlist) - 2 - pivotcounter]
                pivotcounter += 1
            else:
                numcounter += 1
        else:
            numcounter += 1
    return numlist
            
    
testlist = [3, 7, 8, 5, 2, 1, 9, 5, 4]
print(quicksort(testlist))