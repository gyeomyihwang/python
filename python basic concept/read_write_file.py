# 파일 생성하기
# open = "파일이름"과 "파일열기모드" 를 입력값으로 받고 결괏값으로 파일 객체를 돌려줌.
# 파일 객체 = open(파일이름, 파일 열기 모드ㄴ)
# f = open('새파일.txt', 'w') # 새로운 파일이 생김 #@$@#$#@$@#$
# f.close()  # 파일 객체를 닫아주는 역할 @#$@#$#@$

# 파일 열기모드 
r = "읽기모드 - 파일을 읽기만할 때 사용"
w = "쓰기모드 - 파일에 내용을 쓸 때 사용" # 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐
a = "추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용"
 
# 파일을 쓰기 모드로 열어 출력값 적기 (이미 존재하는 파일을 열면 원래 있던 내용 모두 사라짐)
# 예시 1. 파일을 쓰기모드로 열어서 출력값을 적어주기.
f = open("새파일.txt", 'w')
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i # i는 1부터 10까지 들어감.
    f.write(data) # print(data) 가 아님. 즉 새파일.txt에 적은 것.
f.close()
# 예시 2. 일반적으로 모니터 화면에 출력하는 방법. 예시 1과 비교해보기.
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)

# 프로그램 외부에 저장된 파일을 읽는 방법
# 1. readline 함수 이용하기 => 1번째 줄만 출력함
f = open("새파일2.txt", 'r') # 'r' = 읽기모드
line = f.readline()
print(line)
f.close()
# 모든 줄 읽어서 출력하기
f = open('새파일2.txt', 'r')
while True: # 무한루프
    line = f.readline() # 더 읽을 줄이 없으면 빈문자열('') 출력
    if not line: break 
    print(line)
f.close()

# 2. readlines 함수 사용하기 
print(" ========== readline ========= ")
f = open('새파일2.txt', 'r')
lines = f.readlines() # readline 이 아님
print(type(lines)) # list 로 만들어줌
for line in lines:
    print(line)
f.close()
# 줄 끝에 자동으로 붙는 \n 제거하기 => trrip() 사용
print(" ========== readline with strip() ========= ")
f = open('새파일2.txt', 'r')
lines = f.readlines() # readline 이 아님
print(type(lines)) # list 로 만들어줌
for line in lines:
    line = line.strip() # 줄마다 간격 없이 줄바꿈만 됨
    print(line)
f.close()

# 3. read 함수 사용하기
print( '========== read =========')
f = open('새파일2.txt', 'r')
data = f.read() # data = 파일 전체의 내용
print(data)
f.close()

# 파일에 새로운 내용 추가 ('a')
# 예시
f = open('새파일2.txt', 'a')
for i in range(11, 20):
    data = '%d번째 줄입니다.\n' % i # 11 ~ 19 추가
    f.write(data)
f.close()

# with 문과 함께 사용
# 파일을 열고 닫는 것을 자동으로 처리할 수 있음
# 예시
with open("foo.txt", 'w') as f: # with 문을 사용하면 with블록을 벗어나는 순간 f가 자동 close
    f.write('My name is Austin')

with open("foo.txt", 'r') as f:
    content = f.read()
    print(content)
with open("foo.txt", 'a') as f:
    f.write("\nhello!")

# impot sys는 나중에 보기