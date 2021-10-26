# for 문
# for 변수 in 문자열(리스트, 튜플 가능):
#     수행할 문장1
#     수행할 문장2
#     ...

# 예시 1
test_list=['one','two','three']
for i in test_list:
    print(i)
# one
# two
# three

# 예시 2
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)
# 3
# 7
# 11

# for문 응용
# 예시 3 : 총 5명 학생이 시험을 봄. 시험 점수가 60점을 넘으면 합격, 그렇지 않으면 불합격. 합격 여부 보여주기
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print("%d번 학생은 합격입니다." % number)
    else:
        print("%d번 학생은 불합격입니다." % number)
# 1번 학생은 합격입니다.
# 2번 학생은 불합격입니다.
# 3번 학생은 합격입니다.
# 4번 학생은 불합격입니다.
# 5번 학생은 합격입니다.

# for 문 + continue
marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue # 처음으로 돌아감
    else:
        print("%d번 학생 축하합니다. 합격입니다." % number)
# 1번 학생 축하합니다. 합격입니다.
# 3번 학생 축하합니다. 합격입니다.
# 5번 학생 축하합니다. 합격입니다.

# for 문 + range 함수
# range 함수 => a = range(시작 숫자, 끝 숫자(끝 숫자 포함 x))
add = 0
for i in range(1,11):
    add = add + i
print(add) # 55

# 예시 4
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)): # len(marks)는 5 => 0~4
    if marks[number] < 60: # marks 리스트 안에서 number 번째 (0,1,2,3,4)
        continue
    else:
        print("%d번 학생 축하합니다. 합격입니다." % (number + 1)) # number + 1 = 1,2,3,4,5

# for와 range를 사용해 구구단 만들기

for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end=" ") # end=" " => 다음 줄로 넘어가지 않게 하기 위함
    print("")

# List 내포 사용하기
# [표현식 for 항목 in 반복가능객체 if 조건문]
a = [1, 2, 3, 4] # result라는 리스트에 a리스트에 있는 값 * 3 넣기
result = []  #빈 리스트
for num in a:
    result.append(num*3)
print(result) # [3, 6, 9, 12]
# 내포하면
a = [1,2,3,4]
result = [num * 3 for num in a] # 리스트 내포
print(result) # [3, 6, 9, 12]
# 짝수에만 3을 곱하여 담기
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result) # [6, 12]