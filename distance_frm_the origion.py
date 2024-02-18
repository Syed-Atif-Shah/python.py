class Point:
    def __init__(self, x=0, y=0):
        self.a=x
        self.b=y
    def Distance(self, x=0, y=0):
        self.a=x
        self.b=y
        return (self.a**2 + self.b**2)**0.5 #(underroot a^2+b^2) ##logic
    
p1= Point() #an objectr can be deleted by: del p1
DFO=p1.Distance(14,16) 
# here we defined two attributes of the object p1: a,b, #we can delete an attribute of an object by del p1.a | del p1.b
print(DFO)
