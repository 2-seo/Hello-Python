import random

# 0~99까지 숫자 중 20개 샘플
randomList = random.sample(range(100), 20)
numList = [4,3,2,1,0]

def swap(a, b, list):
    data = list[a]
    list[a] = list[b]
    list[b] = data

def bubbleSort(data):
    for i in range(len(data)):
        swaped = False
        for j in range(len(data) -i -1):
            if(data[j] > data[j+1]):
                swap(j, j+1, data)
                swaped = True
        if swaped == False:
            break

bubbleSort(randomList)
bubbleSort(numList)
print(randomList)
print(numList)