# List (리스트 자료형)
# 대괄호 [] 로 감싸주고 ,로 구분
# 특징 : 순서있음. 요소 변경 & 삭제 가능 (mutable)
a = [] # 빈 리스트
a = list() # 빈 리스트
b = [1,2,3] # 요소가 숫자
c = ['My', 'name', 'is', 'Austin'] # 요소가 문자열
d = [1,2,'Austin'] # 요소가 숫자 & 문자열
e = [1,2,['My', 'name']] # 요소가 숫자 + 리스트 자체

# Indexing List (리스트 인덱싱하기)
a = [1,2,3]
print(a) # [1,2,3]
print(a[0]) # 1 # 리스트 a 의 첫 번째 요솟값
print(a[0] + a[2]) # 4 (1 + 3)
print(a[-1]) # 3

a = [1, 2, 3, ['a', 'b', 'c']]
print(a[0]) # 1
print(a[-1]) # ['a', 'b', 'c']
print(a[3]) # ['a', 'b', 'c']
print(a[-1][0]) # a

# 3중 리스트 인덱싱 
a = [1, 2, ['a', 'b', ['My', 'Name']]] 
print(a[2][2][0]) # My

# List Slicing
a = ['a','b','c','d','e']
print(a[0:2]) # ['a', 'b']

# 중첩 리스트 슬라이싱
a = [1,2,3,['a','b','c'],4,5]
print(a[2:5]) # [3, ['a', 'b', 'c'], 4]
print(a[3][:2]) # ['a', 'b']

# 리스트 더하기
a = ['a','b','c']
b = ['d','e','f']
print(a+b) # ['a', 'b', 'c', 'd', 'e', 'f']

# 리스트 곱하기
a = ['a','b','c']
print(a * 3) # ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

# Length
a = ['a','b','c']
print(len(a)) # 3

# 리스트 수정하기 (editing a list)
a = ['a','b','c']
a[2] = 4 # 리스트 a 안의 3번째(c)를 숫자 4로 변경
print(a) # ['a', 'b', 4]

# 리스트 삭제하기 (deleting a content in the list) (del)
a = ['a','b','c']
del a[2]
print(a) # ['a', 'b']

# 리스트에 요소 추가 (append)
a = ['a','b','c']
a.append('d')
print(a) # ['a', 'b', 'c', 'd']
a.append(['e','f'])
print(a) # ['a', 'b', 'c', 'd', ['e', 'f']]

# 리스트 정렬 (sort)
a = [5, 3, 2, 1, 4]
a.sort()
print(a) # [1, 2, 3, 4, 5]
a = ['c','d','a','b','e']
a.sort()
print(a) # ['a', 'b', 'c', 'd', 'e']

# 리스트 뒤집기 (reverse)
a = [5, 3, 2, 1, 4]
a.reverse()
print(a) # [4, 1, 2, 3, 5]

# 리스트 위치 반환 (index)
a = [1, 2, 3]
print(a.index(3)) # 2
print(a.index(1)) # 0

# 리스트 요소 삽입 (insert)
a = ['a','b','c']
a.insert(3, 'd') # 3번째 위치에 'd' 삽입
print(a) # ['a', 'b', 'c', 'd']

# 리스트 요소 제거 (remove(x)) 리스트에서 처음으로 나오는 X 를 삭제
a = ['a','b','c','a','b','c']
a.remove('c')
print(a) # ['a', 'b', 'a', 'b', 'c']

# 리스트 요소 끄집어내기 (pop) 리스트 맨 마지막 요소 돌려주고 그 요소 삭제
# pop()
a = ['a','b','c']
print(a.pop()) # c
print(a) # ['a', 'b']
# pop(x)
a = ['a','b','c']
print(a.pop(1)) # b
print(a) # ['a', 'c']

# 리스트에 포함된 요소 x의 개수 세기 (count)
a = ['a','b','c','a']
print(a.count('a')) # 2

# 리스트 확장 (extend(x)) x 에는 리스트만 올 수 있음
a = ['a','b','c']
a.extend([4,5])
print(a) # ['a', 'b', 'c', 4, 5]
a.extend([6,7])
print(a) # ['a', 'b', 'c', 4, 5, 6, 7]
a = ['a','b','c']