from listFunctions import *

def insertionSort(numlist):
    
    for i in range(len(numlist)):
        if i > 0:
            if numlist[i] < numlist[i - 1]:
                for k in range((len(numlist) + i)- len(numlist)):
                    if numlist[i] < numlist[k]:
                        numlist[i], numlist[k] = numlist[k], numlist[i]
    return numlist
                
            
newList = createList(10)
shuffledlist = shufflelist(newList)
print(f"shuffled list: {shuffledlist}")
print(f"sorted list: {insertionSort(shuffledlist)}")
