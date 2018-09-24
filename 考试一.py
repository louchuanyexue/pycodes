n = input()
if n[-1] in {'J'}:
    b = eval(n[0:-1])/4.186
    print("{:.3f}cal".format(b))
else:
    b = eval(n[0:-3])*4.186
    print("{:.3f}J".format(b))
