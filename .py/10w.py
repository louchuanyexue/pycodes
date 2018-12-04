n=eval(input())
s=input()
t=s.split()
c=[]
for i in range(n):
    c.append(eval(t[i]))
print(max(c),end=" ")
print(min(c))
