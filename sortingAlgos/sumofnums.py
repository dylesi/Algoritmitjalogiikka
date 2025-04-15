def sumofNums(nums):
    returnsum = 0
    for num in str(nums):
        returnsum += int(num)
    print(returnsum)
    return returnsum

def divisibleByNine(nums):
    
    if nums <= 9:
        if nums % 9 == 0:
            return True
        else:
            return False
    else:
        return divisibleByNine(sumofNums(nums))
    
        
print(divisibleByNine(12959271))

