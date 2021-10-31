# 사칙연산 class 만들기 # +,-,/,*
# 먼저 클래스로 만든 객체를 중심으로 어떤식으로 동작하게 할 것인지 미리 구상.

class FourCal:
    def setdata(self, first, second): # function inside a class = called "Method"
        self.first = first # 4가 전달됨 # = a.first = 4
        self.second = second # 2가 전달됨 # = a.second = 2
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def div(self):
        result = self.first / self.second
        return result


a = FourCal()
b = FourCal()
a.setdata(4,2)
b.setdata(3,8)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(b.add())
print(b.mul())
print(b.sub())
print(b.div())