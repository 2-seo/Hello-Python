# .append
# .pop
# .insert
# .clear
myList = ['banana', 'cherry', 'apple']

if 'banana' in myList:
    print('yes')
else:
    print('no')

myList.append('kiwi')
myList.insert(0, 'cake')
print(myList)

item = myList.pop()
print(item)
print(myList)

print('---------------')
myList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# list[a:b]
# a 인덱스 부터
# b 인덱스 전까지 (b 포함 X)
print(myList2[1:3])

print('---------------')
# 제곱 만들기
squareList = [i*i for i in myList2]
print(squareList)

