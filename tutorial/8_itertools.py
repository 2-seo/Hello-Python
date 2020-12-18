# itertools: product, permutations, combinations, accumulate, groupby, infinite iterators
# permutations: 순열
from itertools import product, permutations, accumulate, groupby

# product
a = [1, 2]
b = [3, 4]
prod = product(a, b)
print(list(prod))

prod = product(a, b, repeat=2)
# print(list(prod))

# permutations
list1 =[1, 2, 3]
perm = permutations(list1, 2)
print(list(perm))

# accumulate (축적하다)
list2 = [1, 2, 3, 4]
accu = accumulate(list2)
print(list(accu))

# groupby
def smaller_than_3(x):
    return x < 3

list3 = [1, 2, 3, 4, 5]
group_obj =  groupby(list3, key=smaller_than_3)

for key, value in group_obj:
    print(key, list(value))

person = [
    {
        'name': 'tim',
        'age': 23
    },
    {
        'name': 'kim',
        'age': 23
    },
    {
        'name': 'lisa',
        'age': 25
    },
    {
        'name': 'claire',
        'age': 26
    }
]

group_person = groupby(person, key=lambda x: x['age'])
for key, value in group_person:
    print(key, list(value))
