#单行动态刷新条
from time import *
scale = 100
print("程序开始执行".center(25,'-'))
for i in range (scale+1):
    a = i/scale*100
    b = scale-i
    c = "*"*i
    d = "."*b
    t = clock()
    print("\r{:^3.1f}%[{}->{}]{:.2f}s".format(a,c,d,t),end='')
    sleep(0.05)
print("\n"+"程序执行完毕".center(25,'-'))
