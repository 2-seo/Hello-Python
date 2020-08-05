treeHit = 0
while treeHit<10:
    treeHit += 1
    print("나무를 %d번 쳤습니다" % treeHit)
    if treeHit==10:
        print("나무가 넘어갑니다")

coffee = 10
money = 100
while money:
    coffee -= 1
    print("남은 커피 수량은 %d입니다" %coffee)
    if coffee == 0:
        print("모든 커피 수량이 떨어졌습니다")
        break