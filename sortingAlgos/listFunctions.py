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
