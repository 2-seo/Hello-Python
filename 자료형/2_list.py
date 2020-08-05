# 리스트 []

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호의 인덱스 찾기
print(subway.index("조세호")) # 1

# 값 추가하기
subway.append("하하")

# 사이에 값 추가
subway.insert(1, "정형돈")
print(subway)

# 갑 꺼내기
subway.pop()
print(subway)

# 같은 값이 몇 개인지 확인
subway.append("유재석")
print(subway.count("유재석"))

# 정렬
numList = [5, 4, 3, 2, 1]
numList.sort()
print(numList)

# 순서 뒤집기
numList.reverse()
print(numList)

# 모두 지우기
numList.clear()

# 리스트 합치기
numList = [5, 4, 3, 2, 1]
numList.extend(subway)
print(numList)