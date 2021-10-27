# input (사용자가 입력한 값을 어떤 변수에 대입하기) & print
# print
# input 사용 예시
# a = input() # abcde 넣기 $%%%%%%%%%%%
# print(a) # abcde 출력 %%%%%%%%%%%

# 프롬프트를 띄워서 사용자 입력 받기
#num = input("Type a number here: ") # 12 넣기 @#$$@$@#$@$#$@#$
#print(num) # 12 출력 #@#$#@$@#$@$@#$@#
#print(type(num)) # <class 'str'> # input으로 들어온 것들은 모두 문자열로 취급

# print
# 큰따옴표("")로 둘러싸인 문자열은 + 연산과 동일
print("My" "name" "is Austin") # Mynameis Austin
print("My"+"name"+"is Austin") # Mynameis Austin

# 콤마(,)를 사용하면 문자열 사이에 띄어쓰기 할 수 있음
print("My", "name", "is Austin") # My name is Austin

# 한 줄에 결괏값 출력하기
for i in range(10):
    print(i, end=" ") # 새로운 줄이 아닌 한 줄로 결괏값 출력됨. 숫자 사이에 빈칸 한칸 있음

