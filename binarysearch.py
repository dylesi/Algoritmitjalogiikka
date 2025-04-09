def binarySearch(numlist, target, minimum=0, maximum=None):
    
    if maximum == None:
        maximum = len(numlist) - 1
    if maximum < minimum:
        return -1

    guess = int((maximum + minimum) / 2)

    if numlist[guess] == target:
        return numlist[guess]
    elif numlist[guess] < target:
        return binarySearch(numlist, target, guess + 1, maximum)
    else:
        return binarySearch(numlist, target, minimum, guess -1)

    
numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
print(binarySearch(numlist, 1))