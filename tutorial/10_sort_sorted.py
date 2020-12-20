# reverse = True/False, key=len, key=str.lower, key=func

# sorted => 정렬 후 새로운 객체를 반환
list1 = ['strawberry', 'tomato', 'banana', 'apple', 'coconut']

print(sorted(list1))
print(sorted(list1, reverse=True))
print(sorted(list1, key=len)) # 길이순으로 반환
print(sorted(list1, key=lambda x: x[:-1]))
print(list1) # 원본은 변경되지 않음

print('=======================')

# sort => 정렬 후 객체를 직접 변경
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
list1.sort(key=len)
print(list1)
list1.sort(key=lambda x: x[:-1])
