def valuemap(num, minimum, maximum, newMinimum, newMaximum):
    
    if minimum == newMinimum and maximum == newMaximum:
        return num
    else:
        #factor = (maximum - minimum) / num
        return ((newMinimum + newMaximum) / ((maximum - minimum) / num))
    
    
    
print(valuemap(50, 0, 100, 5, 10))