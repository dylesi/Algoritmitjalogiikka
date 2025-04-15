import random

def createList(amount):
    returnlist = []
    for i in range(1, amount + 1):
        returnlist.append(i)
    return returnlist

def shufflelist(numlist):
    for i in range(len(numlist)):
        randomnum = random.randint(0, len(numlist) - 1)
        numlist[i], numlist[randomnum] = numlist[randomnum], numlist[i]
    return numlist
    
def issorted(shufflelist, comparelist):
    print(f"comparing {comparelist} with {shufflelist}")
    for iter, num in enumerate(shufflelist):
        if comparelist[iter] != shufflelist[iter]:
            return False
        continue
    return True
        


listlength = 10
comparelist = createList(listlength)

iterations = 0
while True:
    uusilista = createList(listlength)
    shuffledlist = shufflelist(uusilista)
    iterations += 1
    
    if issorted(comparelist, shuffledlist):
        print(f"List sorted, it took {iterations} iterations!")
        break
      