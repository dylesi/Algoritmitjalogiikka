def coPrimes(n):
    returnlist = []
    for i in range(1, n):
        if GCD([n, i]) == 1:
            returnlist.append(i)
    return returnlist