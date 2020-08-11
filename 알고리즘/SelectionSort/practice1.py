import random

def selectionSort(data):
    for i in range(len(data)-1):
        lowest = i
        for j in range(i+1, len(data)):
            if data[lowest] > data[j]:
                lowest = j
        swap(i, lowest, data)

def swap(a, b, dataList):
    data = dataList[a]
    dataList[a] = dataList[b]
    dataList[b] = data

list = random.sample(range(100), 20)
print(list)
selectionSort(list)
print(list)