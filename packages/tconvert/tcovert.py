def c2f(tempture):
    return eval("{:.2f}".format(tempture*1.8+32))

def f2c(tempture):
    return eval("{:.2f}".format((tempture-32)/1.8))

if __name__=="__main__":
    t = input()
    if t[-1] == "F":
        print("{}C".format(f2c(eval(t[:-1]))))
    elif t[-1] == "C":
        print("{}F".format(c2f(eval(t[:-1]))))
    else:
        print("输入格式错误")
