# class
# 예시 1. 계산기 더하기 예제; 계산기는 이전에 계산한 값을 항상 메모리 어딘가에 저장할 수 있어야 한다.
result = 0
def add(num):
    global result
    result = result + num
    return result

print(add(3)) # 3
print(add(4)) # 7

# 예시 2. 계산기가 2개 필요한 상황 => 함수를 따로 만들어야함  * 계산기가 10대가 필요한 상황이면 이렇게 하기 힘듦.
result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 = result1 + num 
    return result1 

def add2(num):
    global result2
    result2 = result2 + num
    return result2

print(add1(3)) # 3
print(add1(4)) # 7
print(add2(3)) # 3
print(add2(7)) # 10

# 예시 3. 예시 2를 class 사용 후 쉽게 구현하기
class Calculator:
    def __init__(self):
        self.result = 0
    def add(self, num):
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) # 3
print(cal1.add(4)) # 7
print(cal2.add(3)) # 3
print(cal2.add(7)) # 10

# 가장 간단한 class 예시
class Cookie:
    pass
a = Cookie()
b = Cookie()