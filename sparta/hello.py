# 변수, 자료형, 조건문, 반복문, 기타 라이브러리

print('hello python')

a = 2
b = 3
print(a+b)

first_name = 'Harry'
last_name = 'Bro'
print(first_name,last_name + str(a))

#자료형

# 리스트
a_list = ['사과', '감', '배', ['영희', '철수']]
print(a_list[3][1])
a_list.append('짱구')

#딕셔너리 -> key로 value를 찾음
a_dict = {'name': 'bob', 'age': 24}
print(a_dict['name'])
a_dict['height'] = 180
print(a_dict['height'])

# 딕셔너리 안에 리스트를 담을 수 있음
fruits_list = ['apple', 'banana']
a_dict['fruits'] = fruits_list
print(a_dict['fruits'][1])

# 조건문
age = 24
if age > 20:
    print('성인입니다')
else:
    print('청소년입니다.')

# 반복문
fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

for fruit in fruits:
    print(fruit)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person['name'])

myEmail = 'likeharrybro@gmail.com'
# result = myEmail.split('@')[1].split('.')[0]
result = myEmail.replace('gmail', 'naver')
print(result)


