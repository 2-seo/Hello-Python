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