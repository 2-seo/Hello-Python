# Sets: unordered, mutable, no duplicates

mySet = {1, 2, 2, 3, 4, 5, 5}
print(mySet)

mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(3)
print(mySet)

# 값 지우기
mySet.discard(3)
print(mySet)

# union
print('--- union ---')
odds = {1, 3, 5, 7, 9}
evens = {2, 4, 6, 8, 10}
u = odds.union(evens)
print(u)

# intersection
print('--- intersection --')
i = u.intersection(odds)
print(i)

# difference
print('--- difference ---')
d = u.difference(odds)
print(d)

# update
print('--- update intersection ---')
u.intersection_update(odds)
print(u)

# issubset, issuperset
set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9 ,10}
set2 = {1, 3, 5, 7, 9}
print('--- set1 is subset set2? --- ')
print(set1.issubset(set2))

print('--- set1 is superset set2? --- ')
print(set1.issuperset(set2))
