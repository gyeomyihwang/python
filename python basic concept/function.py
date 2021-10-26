# function (함수)

# def 함수명(매개변수) :
#     <수행할 문장>
#     <수행할 문장>

# 예시 1. 함수 이름은 add이고 입력으로 2개 값을 받으며 결괏값은 2개의 입력값을 더한 값이다.
def add(a,b):
    return a + b # 함수의 결괏값을 돌려주는 명령어
print(add(1,2)) # 3 

# 예시 2. 예시 1과 같은 함수
def add(a, b):
    return a+b
a = 3
b = 7
c = add(a,b)
print(c) # 10

# 매개변수와 인수