#private method usage
#objname._classname__privatemethod
class abc():
    def __init__(self,var):
        self.__var=var #__var means private variable
    def __display(self): #__name() private method
        print("from class method,var",self.__var)
obj=abc(100)
obj._abc__display()
