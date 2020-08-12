def split(data):
    if len(data) < 2:
        return data

    mid = int(len(data) / 2)
    print('mid: {}'.format(mid))
    left = split(data[:mid])
    print('left: {}' .format(left))
    right = split(data[mid:])
    print('right: {}'.format(right))
    return left, right

data = [1,2,3]
left, right = split(data)
print(left, right)