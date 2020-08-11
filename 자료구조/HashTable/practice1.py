storage = [0 for i in range(10)]

def make_hashCode(data):
    return hash(data) % 8

def add(key, data):
    key = make_hashCode(key)
    storage[key] = data

def peek(key):
    key = make_hashCode(key)
    data = storage[key]
    print('Key: {} Data: {}' .format(key, data))

add('seo', '01012341234')
add('kim', '01022223333')
add('lee', '01033334444')

peek('seo')
peek('kim')
peek('lee')
