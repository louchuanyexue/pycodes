n=eval(input())
s=input()
t=[]
t2=[]
for letter in s:
    t.append(letter)
pr = set(t)
c=len(pr)
for i in pr:
    print(i,end='')
    t2.append(i)
if(n-c*2==1):
    print(t2[0],end='')
for i in reversed(t2):
    print(i,end='')
