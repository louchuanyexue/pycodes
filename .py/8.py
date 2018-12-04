m=eval(input())
n=input()
c=[]
for i in range(len(n)):
    c.append(eval(n[i]))
'''for j in range(n):'''
i=len(c)-1
for j in range(len(c)-1):
    if(c[j]!=0):
        print(str(c[j])+"*"+str(m)+'^'+str(i)+'+',end='')
    i=i-1

if(c[len(c)-1]!=0):
    print(str(c[len(c)-1])+'*'+str(m)+'^0')
    
    
