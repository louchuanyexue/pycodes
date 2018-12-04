n=eval(input())
s=input()
t=s.split()
c=[]
a=[]
d=[]
for i in range(n):
    c.append(eval(t[i]))
a.append(-1)
for j in range(n):
    while j<=(n-1):
        if c[i]>=a[-1]:
            a.append(c[i])
    d.append(len(a)-1)
    a=[]
print(max[d])
