s=input().split()
fn=eval(s[0])
tm=eval(s[1])
if tm<5:
    c=0
else:
    c=int(2*(tm/5))
if fn<=3:
    g=10+c
elif  fn<=10:
    g=10+2*(fn-3)+c
elif fn>10:
    g=24+(fn-10)*3+c
print("%d"%g)
    

