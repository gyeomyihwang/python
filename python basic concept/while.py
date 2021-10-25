# while 
# 예시 1. 10번 찍어 안넘어가는 나무 없다.
treehit = 0
while treehit < 10:
    treehit = treehit + 1
    print("나무를 %d번 찍었습니다." % treehit)
    if treehit == 10:
        print("나무 넘어갑니다.")
# 나무를 1번 찍었습니다.
# 나무를 2번 찍었습니다.
# 나무를 3번 찍었습니다.
# 나무를 4번 찍었습니다.
# 나무를 5번 찍었습니다.
# 나무를 6번 찍었습니다.
# 나무를 7번 찍었습니다.
# 나무를 8번 찍었습니다.
# 나무를 9번 찍었습니다.
# 나무를 10번 찍었습니다.
# 나무 넘어갑니다.

# 커피 자판기
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break # while문을 강제로 빠져나감