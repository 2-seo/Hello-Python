import random

rndList = random.sample(range(1,100), 10)
print(rndList)

def sequentialSearch(list, data):
    for i in range(len(list)):
        if data == list[i]:
            return i
    return -1

result = sequentialSearch(rndList, 10)
print(result)