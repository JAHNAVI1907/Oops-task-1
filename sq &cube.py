class square:
    def __init__(self,a):
        self.a=a
    def sq(self):
        return self.a**2
class cube:
    def __init__(self,a):
        self.a=a
    def cub(self):
        return self.a**3
class addition(square,cube):
    def __init__(self,a):
        square.__init__(self,a)
        cube.__init__(self,a)
a=int(input("enter a number:"))
obj=addition(a)
print("square =",obj.sq())
print("cube =",obj.cub())
print("sum of square and cube is :",obj.sq()+obj.cub())
