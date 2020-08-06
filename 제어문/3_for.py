test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

# a = [(1,2), (3,4), (5,6)]
a = [[1,2], [3,4], [5,6]]
for (first,last) in a:
    sum = first + last
    print(sum)
print()

total = 0
for i in range(1, 11):
    total += i
print(total)

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()

print()
# list Comprehension
list = [num for num in range(10)]
print(list)

# 짝수 값만 가져오
numList = [1, 2, 3, 4, 5, 6 ,7 ,8 ,9, 10]
evenNum = [num for num in numList if num % 2 == 0]
print(evenNum)