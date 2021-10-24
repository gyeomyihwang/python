# Set (집합 자료형)
# 순서가 없음 => 인덱싱으로 값 얻기 불가
set_example = set() # 비어있는 집합
print(set_example) # set()
set_example = set([1, 2, 3])
print(set_example) # {1, 2, 3}
set_example = set("Hello")
print(set_example) # {'e', 'o', 'H', 'l'} => 중복 허용 x / 순서가 없음

# Set을 list로 변환
s = set(['a','b','c'])
l = list(s)
print(l) # ['a', 'b', 'c']
print(type(l)) # <class 'list'>

# Set을 튜플로 전환
s = set(['a','b','c'])
t = tuple(s)
print(t) # ('c', 'b', 'a')
print(type(t)) # <class 'tuple'>

# 교집합 구하기 => 중복되는 것 (intersection)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2) # {4, 5, 6}
print(s1.intersection(s2)) # {4, 5, 6}

# 합집합 구하기 (union)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 | s2) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2)) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# 차집합 구하기 (difference)
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 - s2) # {1, 2, 3}
print(s2 - s1) # {8, 9, 7}
print(s1.difference(s2)) # {1, 2, 3}
print(s2.difference(s1)) # {8, 9, 7}

# Set에 값 1개 추가하기 (add)
s = set(['a','b','c'])
s.add('d')
print(s) # {'a', 'd', 'c', 'b'}

# Set에 여러 개 값 추가하기 (update)
s = set(['a','b','c'])
s.update(['d','e','f'])
print(s) # {'a', 'd', 'c', 'b', 'f', 'e'}

# Set에 특정 값 제거하기 (remove)
s = set(['a','b','c'])
s.remove('a')
print(s) # {'c', 'b'}