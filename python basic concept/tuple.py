# Tuple()
# 튜플은 리스트와 다르게 값의 생성, 삭제, 수정 불가능

tuple_example = ()
tuple_example = (1,) # 단 1개의 요소만을 가질 땐 요소 뒤에 콤마를 무조건 붙여야함
tuple_example = (1,2,3)
tuple_example = 1,2,3 # 괄호 생략 가능
tuple_example = ('a','b',('ab','cd'))

# 튜플 인덱싱하기
t = (1, 2, 'a', 'b')
print(t[0]) # 1
print(t[2]) # a

# 튜플 슬라이싱하기
t = (1, 2, 'a', 'b')
print(t[1:]) # (2, 'a', 'b')

# 튜플 더하기
t1 = (1, 2, 'a', 'b')
t2 = (3, 4)
print(t1 + t2) # (1, 2, 'a', 'b', 3, 4)

# 튜플 곱하기
t = (3, 4)
print(t * 3) # (3, 4, 3, 4, 3, 4)

# 튜플 길이 구하기
t = (1, 2, 'a', 'b')
print(len(t)) #4