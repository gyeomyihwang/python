# module
# 1. import 모듈이름
# 모듈 예시 => 아래 함수를 mod1.py에 저장해둠
# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

import mod1
print(mod1.add(3,4)) # 7
print(mod1.sub(4,2)) # 2

# 2. from 모듈 import 모듈 내 함수 
from mod1 import add
print(add(3,4)) # 7

# 3. add와 sub 모두 사용
from mod1 import add, sub 
from mod1 import * # * => 모두 가져옴

import mod1 # 5, 2 출력 => import 하자마자 출력됨
print(mod1.add(3,4)) # 7
print(mod1.sub(4,2)) # 2
 ########

# 클래스나 변수가 포함되어있는 모듈
import mod2
print(mod2.PI) # 3.141592
a = mod2.Math()
print(a.solv(2)) # 12.566368
print(mod2.add(mod2.PI,4.4)) # 7.5415920000000005