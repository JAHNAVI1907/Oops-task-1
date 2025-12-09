#class method, which calls a function defined global namespace
def aaa(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is:",self.var)
    def modify(self):
        self.var=aaa(self.var)
obj=abc(10)
obj.display()
obj.modify()
obj.display()
