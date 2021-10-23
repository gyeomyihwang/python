# Dictionary
# key 와 value 를 한 쌍으로 갖는 자료형
# Key에는 변하지 않는 값, value에는 변하지 않는 값 & 변하는 값 모두 사용가능

dictionary_example = {'key' : 'value'} 
dictionary_example = {'baseball' : '야구'}

dictionary_example = {'name' : 'Austin', 'age' : 90}

# Value 값에 리스트 넣기 가능
dictionary_example = {'a': ['b', 'c', 'd']}

# Dictionary에 쌍 추가하기
a = {1:'a'}
a[2] = 'b' # Dictionary a 에 추가할 key는 2, value는 'b'
print(a) # {1: 'a', 2: 'b'}
a['name'] = 'Austin'
print(a) # {1: 'a', 2: 'b', 'name': 'Austin'}
a[3] = [1, 2, 3]
print(a) # {1: 'a', 2: 'b', 'name': 'Austin', 3: [1, 2, 3]}

# Dictionary 요소 삭제하기 (del)
del a[1] # Dictionary a 에서 key가 1인 요소 삭제하기
print(a) # {2: 'b', 'name': 'Austin', 3: [1, 2, 3]}

# Dictionary 기본 활용
user = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
print(user['name']) # Austin

# Dictionary 주의사항
# 1. 중복되는 Key값 -> 하나를 제외한 나머지 모든 것들이 무시됨
a = {1:'a', 1:'b', 1:'c'}
print(a) # {1: 'c'}
# 2. Key에는 리스트를(변하는 값) 쓸 수 없음, 하지만 튜플은(변하지 않는 값) key로 쓸 수 있다. = 변하는 값인지 아닌지에 달림

# Key 리스트 만들기 (keys) = Dictionary의 key만 모아서 객체를 돌려줌 
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
akeys = a.keys()
print(akeys) # dict_keys(['name', 'age', 'country'])
print(type(akeys)) # <class 'dict_keys'>

# dict_keys 사용법
for k in akeys:
    print(k) #name age country 줄바꿈하며 출력됨

# dicts_key를 리스트로 바꾸기
keys_list = list(a.keys())
print(keys_list) # ['name', 'age', 'country']

# value 리스트 만들기 (values)
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
avalues = a.values()
print(avalues) # dict_values(['Austin', 90, 'Korea'])
print(type(avalues)) # <class 'dict_values'>

# key & value 쌍으로 얻기(items) # 쌍을 튜플로 묶은 값을 dict_items 객체로 돌려줌
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
aitems = a.items()
print(aitems) # dict_items([('name', 'Austin'), ('age', 90), ('country', 'Korea')]) 
print(type(aitems)) # <class 'dict_items'>

# key : value 쌍 모두 지우기 (clear)
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
a.clear()
print(a) # {} => empty dictionary

# Key로 Value 얻기 (get)
# get(x) 함수 = x라는 key에 대응하는 value 돌려줌
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
print(a.get('name')) # Austin ( = a['name'] )
print(a.get('nokey')) # None
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
print(a.get('abc', 'no!!')) # no!! 출력 (dictionary 안에 찾으려는 key값이 없을 경우 미리 정해둔 default값 'no!!'가 가져와짐)

# Key가 dictionary 안에 있는지 조사하기 (in)
a = {'name' : 'Austin', 'age' : 90, 'country' : 'Korea'}
print('name' in a) # True => 'name'이라는 키가 dictionary안에 존재
print('email' in a) # False => 'False'이라는 키가 dictionary안에 존재 X