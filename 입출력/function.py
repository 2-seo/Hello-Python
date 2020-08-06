def add(a,b):
    return  a+b
var1 = add(1,2)
print(var1)

def say():
    print("hi")
say()

def add2(a,b):
    print("%d와 %d의 합은 %d입니다" % (a, b, a+b))
    print("{a}와 {b}의 합은 %d입니다" .format(a=a, b=b) % (a+b))
    print("{}와 {}의 합은 %d입니다".format(a, b) % (a + b))
add2(1,2)

def say_myself(name, age, man=True):
    print("저의 이름은 {}입니다.".format(name))
    print("저의 나이는 {}살 입니다.".format(age))
    if man:
        print("저는 남자입니다.")
    else:
        print("저는 여자입니다.")

say_myself("Lee", 20, False)

a = 1
def test():
    global a
    a += 1
    return a
print(test())
print(a)