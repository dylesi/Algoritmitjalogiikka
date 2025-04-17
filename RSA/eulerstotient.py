from greatestcommondivisor import GCD

def eulerTot(n):
    returnNums = 0
    for i in range(1, n):
        if GCD([n, i]) == 1:
            returnNums += 1
    return returnNums
