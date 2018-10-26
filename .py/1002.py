n=input()
ls=[]
la=[]
lc=[]
t=0
ls=list(n)
for i in ls:
    t+=eval(i)
la=list(str(t))
for i in la:
    if i=='0':
        lc.append("ling")
    elif i=='1':
        lc.append("yi")
    elif i=='2':
        lc.append("er")
    elif i=='3':
        lc.append('san')
        
    elif i=='4':
        lc.append('si')
    elif i=='5':
        lc.append('wu')
    elif i=='6':
        lc.append("liu")
    elif i=='7':
        lc.append("qi")
    elif i=='8':
        lc.append("ba")
    elif i=='9':
        lc.append("jiu")
print(' '.join(lc))
        

    
