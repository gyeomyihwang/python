# Variable (변수)
var_example = 1
var_example = "Austin"
var_example = ['a','b','c']
변수이름 = "변수에 저장할 값"

a = [1, 2, 3] # [1,2,3]값을 가지는 리스트 자료형이 자동으로 메모리에 생성
# => 변수 a는 [1,2,3] 리스트가 저장된 메모리 주소를 가리키게 된다.
# 변수가 가르키는 메모리 주소 구하기
a = [1, 2, 3]
print(id(a)) # 140216455876288

# 리스트 복사하기 
# 잘못된 방법
a = [1,2,3]
b = a 
print(id(a)) # 140238737198336
print(id(b)) # 140238737198336 => a, b 모두 같은 메모 주소를 가르키게 된다.
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 4, 3]
# 방법 1. [:] 이용하기
a = [1,2,3]
b = a[:] # 리스트 전체를 가르키는 [:] 사용
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
a[1] = 4
print(a) # [1, 4, 3]
print(b) # [1, 2, 3] => a 리스트 값의 변화가 b 리스트 값에 영향을 주지않음
# 방법 2. copy 모듈 이용
from copy import copy  # 모듈
a = [1, 2, 3]
b = copy(a)
print(a) # [1, 2, 3]
print(b) # [1, 2, 3]
print(b is a) # False

# 변수를 만드는 다른 방법 
a, b = ('Austin', 'Hwang') # 튜플로 a, b에 값을 대입
print(a) # Austin
print(b) # Hwang
a = b = "Austin"
print(a) # Austin
print(b) # Austin

# 두 변수의 값 바꾸기
a = 3 
b = 5
print(a) # 3
print(b) # 5
a, b = b, a
print(a) # 5
print(b) # 3