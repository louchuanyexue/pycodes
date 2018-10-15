import re
n=input()
i=0
a=0
b=0
while(i!=n):
    s=input()
    match=re.search(r'[PAT]',s)
    if match:
        a+=1
        print("YES")
    else:
        b+=1
        print("NO")
    i+=1

