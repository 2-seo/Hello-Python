# collections: Counter, namedtuple, orderedDict, defaultdict, deque

from collections import Counter, namedtuple, OrderedDict
str1 = 'aaaabbbbcccc'
counter1 = Counter(str1)
print(counter1)

# key
print(counter1.keys())
# values
print(counter1.values())

# namedtuple
Point = namedtuple('point', 'x, y')
pt = Point(1, 2)
print(pt)
print(pt.x, pt.y)

# OrderedDict
orderedDict = OrderedDict()
orderedDict['a'] = 4
orderedDict['b'] = 2
orderedDict['c'] = 3
orderedDict['d'] = 1

print(orderedDict)