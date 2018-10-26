n=eval(input())
d={}
i=0
while(i<n):
    s=input()
    la=s.split(' ')
    d[la[-1]]=d.get(la[-1],la[0]+' '+la[1])
    i+=1
yoyo=list(d.keys())
print(d[str(max([int(i2) for i2 in yoyo]))])
print(d[str(min([int(i3) for i3 in yoyo]))])
        
