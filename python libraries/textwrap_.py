# textwrap.shorten
# 문자열을 특정길이에 맞게 일부분을 [...] 으로 변환시켜 길이를 맞춰줌
# 예시
import textwrap
line = "Hello, my name is Austin and I'm 90 years old"
print(line) # Hello, my name is Austin and I'm 90 years old
line = textwrap.shorten(line, width=15) # 문자열의 길이를 15자리가 넘지 않도록 만들기
print(line) # Hello, my [...]

# textwrap.wrap
# 문자열이 너무 길어질 때 특정 길이에서 줄바꿈을 하게 함.
line2 = 'Hello, my name is Austin!' * 10
print(line2) # 한 줄에 'Hello, my name is Austin!'가 출력됨
a = textwrap.wrap(line2, width = 70)
print(a) # 리스트로 리턴됨 => [안에서 ''와 , 로 70글자씩 구분됨] / 각 단어는 분리되지 않음
print("==========================")

a = textwrap.fill(line2, width=70)
print(a) # textwrap.wrap에선 리스트 안에서 ''와 , 로 구분되었지만 여기선 새로운 줄로 구분됨.

