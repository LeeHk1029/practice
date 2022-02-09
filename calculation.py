
class Calculate:
    def Num1(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result
    def Num2(self, first, second, third):
        self.first = first
        self.second = second
        self.third = third
    def mul_add(self): 
        result = (self.first * self.second) + self.third
        return result
    def add_mul(self):
        result = self.first + (self.second * self.third)
        return result
    def add_bracket_mul(self):
        result = (self.first + self.second) * self.third
        return result
    def mul_add_bracket(self):
        result = self.first * (self.second + self.third)
        return result
a = Calculate()
b = Calculate()

a.Num1(1,2)
b.Num2(1,1,2)

print(a.add())
print(a.mul())
print(b.add_mul())
print(b.add_bracket_mul())
print(b.mul_add())
print(b.mul_add_bracket())