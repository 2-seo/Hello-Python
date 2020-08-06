# 파일 생성하기
f1 = open("새파일.txt", 'w')
f1.close()

# r: 읽기모드 - 파일을 읽기만 할 때 사용
# w: 쓰기모드 - 파일에 내용을 쓸 때 사용
# a: 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

# 파일을 쓰기모드로 열어 출력값 적기
f2 = open("새파일.txt", 'w')
for i in range(1, 10):
    data = "%d번째 줄입니다 \n" % i
    f2.write(data)
f2.close()

# readline() : 첫 번째 줄 가져옴
f3 = open("새파일.txt", 'r')
data = f3.readline()
print(data)

while True:
    line = f3.readline()
    if not line: break
    print(line)
f3.close()

# readlines() : 파일의 모든 줄을 읽어서 각각의 줄을 요소로 갖는 리스트로 반환함
f4 = open("새파일.txt", 'r')
lines = f4.readlines()
for line in lines:
    print(line)
f4.close()

# 파일에 새로운 내용 추가하기
f5 = open("새파일.txt", 'a')
for i in range(10, 20):
    data = "%d번째 줄입니다" % i
    f5.write(data)
f5.close()

# with문 : 자동으로 close() 해줌
with open("새파일.txt", 'w') as f6:
    f6.write("Life is too short")
