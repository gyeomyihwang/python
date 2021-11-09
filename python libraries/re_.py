# 정규표현식 (re)
# = 복잡한 문자열을 처리할 때 사용하는 기법

# 예시 1. 주민번호 뒷자리 *으로 변경하기
data = """
a 800905-1234567
b 700905-1234567
"""
# 정규표현식 없이
result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-" + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))
print("\n".join(result))
#a 800905-*******
#b 700905-*******

# 정규식 사용
import re

data2 = """
c 800905-1234567
d 700905-1234567
"""
pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data2))
