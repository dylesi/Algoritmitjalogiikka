import math

def frequency(num):
    return (math.pow(2, ((num - 49) / 12)) * 440)

print(frequency(40))