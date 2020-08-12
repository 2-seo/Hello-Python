# recursive
def fibo(num):
    if num < 2:
        return num
    return fibo(num-1) + fibo(num-2)

print(fibo(6))

# Dynamic Programing
def fibo_dp(num):
    cache = [0 for i in range(num+1)]
    print(cache)
    cache[0] = 0
    cache[1] = 1
    for i in range(2, num+1):
        cache[i] = cache[i-2] + cache[i-1]
        print('cache[{}]: {}'.format(i, cache[i]))
    return cache[num]

fibo_dp(10)