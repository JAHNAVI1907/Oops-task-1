class factorial:
    def __init__(self):
        self.n=int(input("enter a number:"))
        self.f=1
class First(factorial):
    def fact(self):
        for i in range(1,self.n+1):
            self.f=self.f*i
class Second(First):
    def result(self):
        print("result of Factorial is:",self.f)
obj=Second()
obj.fact()
obj.result()
