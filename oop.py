class First:
    def __init__(self,x=0,y=0):
        self.a=x
        self.b=y
    def sum(self,x=0,y=0):
        self.a=x
        self.b=y
        print(self.a+self.b)

obj =First()
obj.sum()
obj.sum(10,20)