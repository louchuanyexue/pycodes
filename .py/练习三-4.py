n = input()
a = eval(n[0:])
b=1
s="*"
print("*".center(a," "))
while b<a:
    b=b+2
    s=s+"**"
    print(s.center(a," "))
