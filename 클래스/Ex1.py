class ForCalc:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def sub(self):
        result = self.first - self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def div(self):
        result = self.first / self.second
        return result
a = ForCalc(2,4)
var1 = a.add()
var2 = a.sub()
var3 = a.mul()
var4 = a.div()
print(var1)
print(var2)
print(var3)
print(var4)
