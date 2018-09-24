from math import *
n = input()
a = eval(n[0:])
b = a/1000+1
e = 1-a/1000
c = pow(b,365)
d = pow(e,365)
f = c/d
f = int(f)
print("{:.2f},{:.2f},{}".format(c,d,f))

