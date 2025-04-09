def collatz(num, iterations = 0):
    
    print(num, end=" ")
    if num == 1:
        return iterations
    if num % 2 == 0:
        iterations += 1
        return collatz(int(num/2), iterations)
    elif num % 2 == 1:
        iterations += 1
        return collatz((num * 3) + 1, iterations)
    
    
print(collatz(27))
    
    