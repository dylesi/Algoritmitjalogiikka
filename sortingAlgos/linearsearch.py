def linearSearch(target, numlist):
    for iterator, num in enumerate(numlist):
        if num == target:
            return iterator
        
numlist = [1,2,3,4,5,6,7,7,8,9,9,10,23]
print(linearSearch(2, numlist))