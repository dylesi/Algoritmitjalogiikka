from coprimes import coPrimes
from congruence import congruence

def carmichael(n):
    a = coPrimes(n)
    m = 1
    trueAmount = 0

    while trueAmount < len(a):
        for coPrime in a:
            if congruence(coPrime ** m, 1, n) == True:
                trueAmount += 1
            else:
                m += 1
    return m