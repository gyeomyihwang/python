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

# 매개변수(parameter) 와 인수(arguments)
# 예시 3.
def add(a, b): # a, b는 매개변수(parameter)
    return a+b
print(add(3,4)) # 3, 4는 인수(arguments)

# 함수 종류 1. 일반적인 함수
def add(a, b): # 함수이름(매개변수):
    c = a + b  # 수행할 문장
    return c   # 결과값

# 함수 종류 2. 입력값이 없는 함수
def greeting():
    return 'Hello'
a = greeting()
print(a) #Hello 출력

# 함수 종류 3. 결괏값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다."%(a, b, a+b))
    print(a, ", ", b, "의 합은 ", a+b, "입니다.", sep="")
add(3,4) # 3, 4의 합은 7입니다.

# 함수 종류 4. 입력값과 결괏값 모두 없는 함수
def greeting():
    print('Hello!')
greeting() #Hello

# 매개변수 지정하여 호출하기
def add(a, b):
    return a+b
result = add(a=3, b=7)
print(result) # 10
result = add(b=7, a=3) # 순서에 상관없이 사용할 수 있음
print(result) # 10

#입력값 몇 개가 될지 모를 때
# def 함수이름(*매개변수):
#     수행할 문장
# 예시. 여러 개의 입력값을 모두 더하는 함수를 만들기
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(add_many(1,2,3,4,5,6,7,8,9,10)) # 55

# 예시. 더하기나 곱하기 정해서 리턴하기
def cal(choice, *num):
    if choice == "add":
        result = 0
        for i in num:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in num:
            result = result * i
    else:
        result = "error"
    return result
ans1 = cal("add", 1,2,3,4,5)
ans2 = cal("mul", 1,2,3,4,5)
print(ans1) # 15
print(ans2) # 120

# 함수의 결괏값은 항상 1개
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3, 4)
print(result) # (7, 12) => 튜플로 값을 가짐
# 받은 하나의 튜플 값을 2개의 결괏값처럼 받기
print(result) # (7, 12)
result1, result2 = add_and_mul(3,4)
print(result1) # 7
print(result2) # 12

# return 사용해서 함수 빠져나가기
def say_nick(nick):
    if nick == "바보":
        return # 입력값으로 바보가 들어오면 문자열을 출력하지 않고 함수를 즉시 빠져나감
    print("나의 별명은 %s 입니다." % nick)

say_nick('바보') # 아무것도 출력이 되지않음
say_nick("Austin") # 나의 별명은 Austin 입니다.

# 매개변수 (parameter) 초깃값 미리 설정하기
def say_myself(name, age, man=True): # 초기화시키고 싶은 매개변수는 항상 뒤쪽에 놓기
    print("My name is %s." % name)
    print("I am %d years old." % age)
    if man:
        print("And I am a man.")
    else:
        print("And I am a woman.")
say_myself("Austin", 95) # 출력값 같음
say_myself("Austin", 95, True) # 출력값 같음
# My name is Austin.
# I am 95 years old.
# And I am a man.

# 함수 속 변수의 효력 범위
a = 1
def add(a):
    a = a + 1 # 새로 업데이트되는 a라는 변수의 값은 함수 안에서만 효력이 있는 함수만의 변수임
add(a)
print(a) # 2가 아닌 1이 나옴

def addsec(f):
    f = f + 1
#print(f) 를 하면 error 뜸.f 변수를 찾을 수 없음. f변수는 오직 함수 안에서만 찾을 수 있음.

# 함수 안에서 함수 밖의 변수를 변경하기
# 방법 1. return 사용하기
a = 1
def add(a):
    a = a + 1
    return a # return을 활용해서 변수 변경시킴
print(a) # 1
a = add(a)
print(a) # 2
# 방법 2. global 명령어 사용하기
a = 1
def add():
    global a # 함수 안에서 함수 밖의 변수 a를 직접 사용하겠다는 뜻 # 비추; 함수는 독립적으로 존재하는게 좋음
    a = a + 1
add()
print(a) # 2

# lambda # 함수를 한줄로 간결하게 만들기 위해 사용
# lambda 매개변수1, 매개변수2, ...: 매개변수를 위한 표현식
# lambda 예시
add = lambda a, b: a+b # return 이 없어도 결과값을 돌려줌
result = add(3,4)
print(result) #7
# 위 lambda 예시와 동일
def add(a, b):
    return a + b
result = add(3,4)
print(result) # 7