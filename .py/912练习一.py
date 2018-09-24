import random
r,s=eval(input())
c=''
random.seed(r+s)
for i in range(20):
    c+=chr(random.randint(32,127))
print(c)
