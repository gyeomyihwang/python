# 파일 생성하기
# open = "파일이름"과 "파일열기모드" 를 입력값으로 받고 결괏값으로 파일 객체를 돌려줌.
# 파일 객체 = open(파일이름, 파일 열기 모드ㄴ)
# f = open('새파일.txt', 'w') # 새로운 파일이 생김 #@$@#$#@$@#$
# f.close()  # 파일 객체를 닫아주는 역할 @#$@#$#@$

# 파일 열기모드 
r = "읽기모드 - 파일을 읽기만할 때 사용"
w = "쓰기모드 - 파일에 내용을 쓸 때 사용" # 해당 파일이 이미 존재할 경우 원래 있던 내용이 모두 사라짐
a = "추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용"
 
# 파일을 쓰기 모드로 열어 출력값 적기
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
# 1. readline 함수 이용하기