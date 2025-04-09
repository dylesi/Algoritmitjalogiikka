from listFunctions import *

def quicksort(numlist):
    pivot = numlist[0]
    numlist.pop(0)
    leftside = []
    rightside = []
    
    for num in numlist:
        if num > pivot:
            rightside.append(num)
        else:
            leftside.append(num)
    
    if len(rightside) > 1:
        rightside = quicksort(rightside)
    if len(leftside) > 1:
        leftside = quicksort(leftside)
    
    templist = []
    templist += (leftside)
    templist += [pivot]
    templist += rightside
    
    return templist
    
shuffledlist = shufflelist(createList(20))
print(f" shuffled list: {shuffledlist}")
print(f" sorted list {quicksort(shuffledlist)}")