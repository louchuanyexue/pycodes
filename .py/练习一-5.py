n = input()
t = n[3:]
if n[0:3] in ['RMB']:
    u = eval(t)/6.78
    print("USD{:.2f}".format(u))
else:
    u = eval(t)*6.78
    print("RMB{:.2f}".format(u))
    
