# textwrap.shorten
# 문자열을 특정길이에 맞게 일부분을 [...] 으로 변환시켜 길이를 맞춰줌
# 예시
import textwrap
line = "Hello, my name is Austin and I'm 90 years old"
print(line) # Hello, my name is Austin and I'm 90 years old
line = textwrap.shorten(line, width=15) # 문자열의 길이를 15자리가 넘지 않도록 만들기
print(line) # Hello, my [...]