class student():
    def __init__(self,name):
        self.name=name
        self.marks=[]
    def entermarks(self):
        for i in range(3):
            m=int(input())
            self.marks.append(m)
    def display(self):
        print(self.name, "got",self.marks )
obj=student("janu")
obj.entermarks()
obj2=student("uma")
obj2.entermarks()
obj.display()
obj2.display()
