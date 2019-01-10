sn = input()
st1 = input()
st2 = input()
snlist = sn.split()
st1list = st1.split()
st2list = st2.split()
snw = int(snlist[0])
snh = int(snlist[1])
st1w = int(st1list[0])
st1h = int(st1list[1])
st2w = int(st2list[0])
st2h = int(st2list[1])

while snh != 0:
    snw = snw+snh
    if snh == st1h:
        snw = snw - st1w
        if snw < 0:
            snw = 0
    if snh == st2h:
        snw = snw - st2w
        if snw < 0:
            snw = 0
    snh = snh - 1
print(snw)