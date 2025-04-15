def pairsOf(nums):
    zeroes = 0
    result = 0
    for num in str(nums):
        if num == "1" and zeroes:
            result = result + zeroes  
        else:
            zeroes += 1
    return result
            
num = "0101101001"
print(pairsOf(num))
    