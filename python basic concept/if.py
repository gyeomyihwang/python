# if 조건문
# else 없이 독립적으로 사용 불가

# 예시 1 : 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.
money = True # 택시를 타라 출력
if money: # True 이면 실행
    print("택시를 타라") # 들여쓰기
else: # False 이면 실행
    print("걸어 가라") # 들여쓰기

# 조건문 = 참과 거짓을 판단하는 문장
x = 3
y = 2
print(x > y) # True
print(x < y) # False
print(x != y) # True

# 예시 2 : 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라
money = 2000 
if money >= 3000:
    print("택시를 타라")
else:
    print("걸어가라") # 걸어가라가 출력됨

# or
# x or y = x 와 y  둘중 하나만 참이어도 참이다
# and 
# x and y = x 와 y 모두 참이어야 참이다
# not x
# x가 거짓이면 참이다

# 예시 3 : 3000원 이상이 있거나 카드가 있따면 택시를 타고 그렇지 않으면 걸어가라
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타라") # 택시를 타라 출력
else: 
    print("걸어가라")

# x in s / x not in s
# 리스트에 적용
print(1 in [1,2,3]) # True
print(1 not in [1,2,3]) # False
# 튜플에 적용
print(1 in (1, 2, 3)) # True
# 문자열에 적용
print("j" in 'python') # False
# 예시 3 : 만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라") # 택시를 타고 가라 출력
else:
    print("걸어가라")

# pass => 아무런 일도 하지 않게 설정하기
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket: # 아무 결괏값도 보여 주지 않음
    pass
else:
    print("카드를 꺼내라")

# elif (개수 제한 없음)
# 예시 4. else를 사용해 주머니에 돈이 있으면 택시, 돈이 없어도 카드가 있으면 택시, 돈도 카드도 없으면 걸어 가라.
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 탁고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
# 예시 5. elif를 사용해 주머니에 돈이 있으면 택시, 돈이 없어도 카드가 있으면 택시, 돈도 카드도 없으면 걸어 가라.
pocket = ['paper', 'handphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# if문을 한 줄로 표현하기
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")
# 한줄로 표현
if 'money' in pocket: pass
else: print("카드를 꺼내라")

# 조건부 표현식 (conditional expression)
if score >= 60:
    message = "success"
else:
    message = "failure"
# 조건부 표현식 사용
message = "success" if score >= 60 else "failure"
# = 조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우