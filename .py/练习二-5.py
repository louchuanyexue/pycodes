n=input()
if n[-1] in {'m'}:
    b=eval(n[0:-1])*39.37
    print("{:.3f}in".format(b))
else:
    b=eval(n[0:-2])/39.37
    print("{:.3f}m".format(b))
