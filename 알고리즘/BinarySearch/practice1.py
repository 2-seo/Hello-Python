def binarySearch(dataList, data):
    if len(dataList) == 1 & dataList[0] == data:
        return True
    elif len(datalist) == 1 & dataList[0] != data:
        return False
    if len(dataList) == 0:
        return False

    middle = len(dataList) // 2
    if dataList[middle] > data:
        return binarySearch(dataList[:middle], data)
    elif dataList[middle] < data:
        return binarySearch(dataList[middle:], data)
    else:
        return True

datalist = [1,2,3,4,5,6,7,8,9,10]
result = binarySearch(datalist, 11)
print(result)
