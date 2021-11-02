# 구구단

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i += 1
    print(result)


gugu(2) # [2, 4, 6, 8, 10, 12, 14, 16, 18]
gugu(3) # [3, 6, 9, 12, 15, 18, 21, 24, 27]
