# lambda arguments: expression
add10 = lambda x: x + 10
print(add10(10))

mul = lambda x, y: x * y
print(mul(10, 2))

points2D = [(1, 2), (3, 4), (2, 5), (10, 1)]

points_sorted = sorted(points2D)
print(points_sorted)

points_sorted = sorted(points2D, key=lambda x: x[1])
print(points_sorted)

# map(func, seq)
list1 = [1, 2, 3, 4, 5]
list2 = map(lambda x: x * x, list1)
print(list(list2))

# filter(func, seq)
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list3_filter = filter(lambda x: x%2==0, list3)
print(list(list3_filter))

# reduce(func, seq)
