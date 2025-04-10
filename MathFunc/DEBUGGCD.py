from binarysearch import binarySearch

resultlist = [[1, 2, 7, 14], [1, 2, 4, 8, 16], [1, 2, 3, 4, 6, 8, 12, 24], [1, 2, 4, 8, 16, 32]]

for list in resultlist[1::]:
    print(list)
    for num in range(len(resultlist[0])-1,-1,-1):
        if binarySearch(list, resultlist[0][num]) != -1:
            print(resultlist[0][num])
            break
