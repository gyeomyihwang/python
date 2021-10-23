# String (문자열)
str_example = "Hello, World!"
str_example = "123"
str_example = "abc"

# How to make a string?
str_example = "Hello World"
str_example = 'Hello World'
str_example = """Hello World"""
str_example = '''Hello World'''

# What if we want to put " " or ' ' in a string?
str_example = "Austin's World"
str_example = 'My "name" is Austin'
str_example = 'Austin\'s World'
str_example = "My \"name\" is Austin"

# Change the line - escape code \n
str_example = "My name is Austin\nI'm from Korea."

# Change the line - """ & '''
str_example = """My name is Austin
I'm from Korea
"""

# Insert tab in the line - escape code \t
str_example = "Hello\tWorld" # Hello    world

# Concatenation (문자열 더해서 연결시키기)
a = "My name"
b = " is Austin"
print(a + b) # My name is Austin

# 문자열 곱하기
a = "Austin"
print(a * 2) #AustinAustin

# Length of a string (문자열 길이 구하기)
str_example = "abcde"
print(len(str_example)) #5

# String indexing
str_example = "abcdefg"
#abcdefg
#0123456 (counting from zero. 0부터 순서 계산)
print(str_example[3]) #d
print(str_example[-1]) #g -1 = 뒤에서 첫번째

# String slicing 
str_example = "Austin is my name"
print(str_example[0] + str_example[1]) #Au (not slicing)
print(str_example[0:2]) #Au (slicing) 
# a[start_index : end_index] ***** end index isn't included # (끝번호 해당 x)
print(str_example[7:11]) #is m
print(str_example[:4]) #Aust
print(str_example[3:]) #tin is my name
print(str_example[11:-2]) #y na

# Slicing practice
a = "Ausjin" # Question: Change Ausjin to Austin!
print(a[:3] + "t" + a[4:]) # Austin

# String formating (문자열 포메팅) 
# 1. putting a number (숫자 바로 대입)
a = "I have %d phones" % 5
print(a) #I have 5 phones
# 2. putting a string (문자열 바로 대입)
a = "I have %s phones" % "five"
print(a) #I have five phones
# 3. putting variable which contains a number (숫자 값이 들어가있는 변수를 대입)
num = 5
a = "I have %d phones" % num
print(a) #I have 5 phones
# 4. putting more than 1 things (2개 이상 값 대입)
num = 5
num_str = "five"
a = "I have %d phones. I have %s phones" % (num, num_str) # 괄호안에 넣어줌, 콤마로 구분
print(a) #I have 5 phones. I have five phones
# 5. %%
a = "Your score : %d%%" % 93
print(a) # Your score : 93%

# String Formating 정리
# %s = string #숫자나 소수를 넣어도 문자열로 변환함
# %c = character 
# %d = integer 
# %f = floating point 
## %% = 문자 "%"