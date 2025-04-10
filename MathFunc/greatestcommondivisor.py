
from quicksort import quicksort
from binarysearch import binarySearch
import random

def GCD(nums):

    #Send the array of numbers to be sorted from smallest to highest
    nums = quicksort(nums)

    #Early returns if the smallest number is less than 0 or 1
    if nums[0] < 0:
        return None
    if nums[0] == 1:
        return 1

    #Assemble divisors from the numbers by checking the modulo of i from the digit
    divisorlist = []
    resultlist = []
    for number in nums:
        for i in range(1, number + 1):
            if number % i == 0:
                divisorlist.append(i)
        resultlist.append(divisorlist)
        divisorlist = []


    commonNum = 0
    foundFlag = 0

    #Start from the smallest numbers' array that we got when we sorted the original numbers list at the start.
    #And iterate it from the largest to the smallest.
    for num in range(len(resultlist[0])-1,-1,-1):

        #Early return if the number is not found on the other numbers array of divisors
        if foundFlag == len(resultlist) - 1:
            break
        #Iterate through every list except the first one
        for list in resultlist[1::]:
            #Send the list to scan through and the largest number of the smallest numbers array
            #to binarysearch and look if the number is within that list.
            #If its not, set the flag to zero and go to the next largest number
            if binarySearch(list, resultlist[0][num]) == -1:
                foundFlag = 0
                break
            #if its gound in the list, save the number to a variable and mark it as found
            else:
                commonNum = resultlist[0][num]
                foundFlag += 1
    #If the code manages to iterate through all the arrays, then we know for sure
    #to return the commonNum which is the correct greatest common divisor
    return commonNum
                

                

#nums = [random.randint(50,54) for randnum in range(10)]

print(GCD([6, 8, 24, -25, 96]))


