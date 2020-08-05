test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)

a = [(1,2), (3,4), (5,6)]
for (first,last) in a:
    sum = first + last
    print(sum)

total = 0
for i in range(1, 11):
    total += i
print(total)

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print(i*j, end=" ")
    print()