def c2f(x):
    F=x*1.8+32
    return ("{:.2f}".format(F))

def f2c(x):
    C=(x-32)/1.8
    return ("{:.2f}".format((C)))

if __name__=="__main__":
    t = input()
    if t[-1] == "F":
        print("{}C".format(f2c(eval(t[:-1]))))
    elif t[-1] == "C":
        print("{}F".format(c2f(eval(t[:-1]))))
    else:
        print("输入格式错误")
