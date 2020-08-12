def quickSort(data):
    if len(data) < 2:
        return data
    left, right = [], []
    pivot = data[0]
    for i in range(1, len(data)):
        if pivot > data[i]:
            left.append(data[i])
        else:
            right.append(data[i])
    return quickSort(left) + [pivot] + quickSort(right)

# list comprehension으로 작성
def quickSort2(data):

    if len(data) < 2:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]
    return quickSort2(left) + [pivot] + quickSort2(right)

# pointer 이용
def quickSort3(data):
    start = 0
    end = len(data)-1
    pivot = data[0]



import random

rndNum = random.sample(range(100), 10)
print(quickSort(rndNum))
print(quickSort2(rndNum))
