dic = {"name": "Lee", "phone": "01012341234"}
print(dic)

a= {"num": [1,2,3]}
print(a)

# 쌍 추가하기
a[2] = [4,5,6]
a["key"] = "value"
print(a)


# 삭제하기
del a["key"]
print(a)

# 함수들
print(a.keys())
print(a.values())
print(a.items())
#key로 value 얻기
value1 = a.get(2)
print(value1)
# 해당 key가 dictionaly에 있는지 확인
var = 'num' in a
print(var)