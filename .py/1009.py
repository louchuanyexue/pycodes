class ConvertClass:
    def __init__(self,count,name):
        self.count = count
        self.name = name
    def convert(self,n):
        if n[-3:]=="CNY":
            self.name="EUR"
            self.count=eval(n[:-3])/7.8942
            return print("{:.2f}{}".format(self.count,self.name))
        elif n[-3:]=="EUR":
            self.name="CNY"
            self.count=eval(n[:-3])*7.8942
            return print("{:.2f}{}".format(self.count,self.name))
        else:
            return print("格式错误")
dc=ConvertClass(7.8942,"EUR")
dc.convert(input())
    
