
from quicksort import quicksort
from binarysearch import binarySearch
import random

def GCD(nums):

    nums = quicksort(nums)

    divisorlist = []
    resultlist = []
    for number in nums:
        for i in range(1, number + 1):
            if number % i == 0:
                divisorlist.append(i)
        resultlist.append(divisorlist)
        divisorlist = []

    print(resultlist)
    commonNum = 0
    foundFlag = 0
    for num in range(len(resultlist[0])-1,-1,-1):
        if foundFlag == len(resultlist) - 1:
            break
        for list in resultlist[1::]:
            if binarySearch(list, resultlist[0][num]) == -1:
                foundFlag = 0
                break
            else:
                commonNum = resultlist[0][num]
                foundFlag += 1
    print(commonNum)
                

                

#nums = [random.randint(50,54) for randnum in range(10)]

GCD([16, 8, 24, 48, 96])


