class Echo:
    def __init__(self,name):
        self.name=name
    def __pow__(self,other):
        if eval(other.name)==0:
            return print("Hello!")
        else:
            return print("Hello {}!".format(", ".join(((" "+dc1.name)*eval(dc2.name)).split())))
s=input()
dc1=Echo(s.split()[0])
dc2=Echo(s.split()[1])
pow(dc1,dc2)
        
