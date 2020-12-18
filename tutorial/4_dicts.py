# Dictionary: Key-Value pairs, Unordered, Mutable

myDict = {
    'name': 'Harry',
    'age': 20,
    'city': 'Seoul'
}

myDict2 = dict(name='marry', age=22, city='Busan')

print(myDict)
print(myDict2)

# 키 벨류 새로 추가
myDict['email'] = 'myemail@gmail.com'
print(myDict)

# 키 삭제
del myDict['email']
print(myDict)

print('-----------------')
name = myDict.pop("name")
print(name)
print(myDict)

print('마지막 키 삭제')
myDict.popitem()
print(myDict)

print('------- key -------')
for key in myDict2:
    print(key)

print('------- value -------')
for value in myDict2.values():
    print(value)

print('----- key value -----')
for key, value in myDict2.items():
    print(key, value)
