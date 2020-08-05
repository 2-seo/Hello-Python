# 문자열
a = '나는 문자열입니다'
print(a)

b = "나도 문자열입니다"
print(b)

c = """나도 문자열이고
여러줄을 작성할 수 있습니다"""
print(c)

jumin = "990120-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2])
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print("뒤 7자리(뒤에서부터): " + jumin[-7:])

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # 전부 소문자로 , 원본 값은 바꾸지 않음
print(python.upper()) # 전부 대문자로 , 원본 값은 바꾸지 않음
print(python[0].isupper()) # true
print(len(python)) # 17
print(python.replace("Python", "Java"))

index = python.index("n")
print(index) # 5
index = python.index("n", index + 1)
print(index) # 15

print(python.find("Java")) # -1, 값이 없으면 -1 반환
#print(python.index("Java")) # 에러 출력후 종료

print(python.count("n")) # n이 총 몇 번 나왔는지 반환, 2

# 문자열 포멧
print("a" + "b") # ab
print("a", "b") # a b

# 방법 1
print("나는 %d살입니다." % 20) # 정수 반환
print("나는 %s를 좋아해요" % "파이썬")
print("Apple은 %c로 시작해요" % "A") # C 문자 하나
print("%s" % "20살")
print("%s" % 30)

# 방법 2
print("나는 {}살입니다." .format(20))
print("나는 {}색과 {}색을 좋아합니다" .format("빨강", "파랑"))
print("나는 {1}색과 {0}색을 좋아합니다" .format("빨강", "파랑"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아합니다" .format(age=20, color="red"))

# 방법 4 (v3.6 이상~)
age = 21
color = "blue"
print(f"나는 {age}살이며, {color}색을 좋아합니다")

# 탈출 문자
print("백문이 불여일견 \n백견이 불여일타")
# print('저는 "사람"입니다')
print("저는 \"사람\"입니다")

# 문장내에서 \
print("c:\\")

# \r 커서를 맨 앞으로 이동
print("Red Apple\rpine") # pine

# \b 백스페이스 한 글자 삭제
print("Applee\b")

# \t 탭
print("Red\tApple")