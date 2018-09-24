from math import *
n = input()
b = eval(n[0:])
c = fabs(b)
d = c+10
e = c-10
f = c*10
if b>=0:
    d=fabs(d)
    e=fabs(e)
    f=fabs(f)
else:
    d=fabs(d)*(-1)
    e=fabs(e)*(-1)
    f=fabs(f)*(-1)
print(int(c),int(d),int(e),int(f))
    
    
