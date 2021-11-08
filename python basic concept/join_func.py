# join => 리스트에 있는 요소들을 모두 합쳐 하나의 문자열로 바꿔줌
a = ["A", "b", "C"]
b =  "@".join(a)
print(b) # A@b@C
c = ".\n".join(a)
print(c) # A.b.C  .과 함께 줄바꿈해서 출력됨