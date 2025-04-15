import random

def createList(amount):
    returnlist = []
    for i in range(1, amount + 1):
        returnlist.append(i)
    return returnlist


def shufflelist(numlist):
    returnlist = []
    
    while numlist:
        randomnum = random.randint(0, len(numlist)- 1)
        returnlist.append(numlist[randomnum])
        numlist.pop(randomnum)
    return returnlist



def bubbleSort(numlist):
    for i in range(len(numlist) - 1):
        for k in range(len(numlist) - i):
            if numlist[i] > numlist[i + k]:
                #print(f"numlist[i]: {numlist[i]} , numlist[k]: {numlist[k]}")
                numlist[i],numlist[i + k] = numlist[i + k], numlist[i]
    return numlist
                
#newList = createList(10)
#shuffledlist = shufflelist(newList)
            
numlist = [10,9,8,7,6,5,4,3,2,1]
print(bubbleSort(numlist))
