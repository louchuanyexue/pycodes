class Creature:
    count=0
    def __init__(self,weight,length,width,height):
        self.weight=weight
        self.length=length
        self.width=width
        self.height=height
        Creature.count+=1
    def pt(self,):
        return self.weight/((pow(0.5*max(self.length,self.width),2)*3.14159*self.height)/3)
a=0
try:
    s = input()
    while s!="":
        weight,length,width,height=tuple(s.split())
        dc=Creature(eval(weight),eval(length),eval(width),eval(height))
        a+=dc.pt()
        s=input()
except:
    pass
print("{:.2f}".format(a/Creature.count))
    
        
