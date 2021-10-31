def add(a, b):
    return a + b

def sub(a, b):
    return a - b


if __name__ == "__main__": # 대화형 인터프리너 & 다른 파일에서 이 모듈을 불러 사용할 때엔 거짓이 되어 수행되지 않음
    print(add(1,4))
    print(sub(4,2))
# 대화형 인터프리너나 다른 파일에서 이 모듈을 불러 사용하면 __name__변수에는 mod1.py의 모듈 이름 값 mod1이 저장됨