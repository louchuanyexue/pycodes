from time import *
jjl = 10
print("开始运行")
for i in range(jjl+1):
    a = i*'**'
    b = (jjl-i)*'..'
    c = (i/jjl)*100
    print("%{:3.0f} [{}->{}]".format(c,a,b))
    sleep(0.1)
print("运行结束")
