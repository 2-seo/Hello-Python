import random

randomNumList = random.sample(range(100), 5)
numList =[1,2,3,4,5]
def sum(numList):
    if len(numList) > 1:
        return numList[0] + sum(numList[1:])
    return numList[0]

def sum2(numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    return total

# total = sum2(randomNumList)
total1 = sum(numList)
total2 = sum2(numList)
print(total1)
print(total2)