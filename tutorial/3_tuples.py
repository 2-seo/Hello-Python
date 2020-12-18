# tuple is immutable

# .index()
# .count()

myTuple = ('a', 'p', 'p', 'l', 'e')
print(type(myTuple))
print(myTuple.count('p')) # tuple 안에 개수를 셈

# 거꾸로 가져오기
print(myTuple[::-1])

# 변수에 한번에 담기
myTuple2 = ('max', 19, 'boston')
name, age, city = myTuple2
print(name, age, city)