t = input()
if t[0] in ['F']:
    te=(eval(t[1:])-32)/1.8
    print('C{:.2f}'.format(te))
else:
    te=eval(t[1:])*1.8+32
    print('F{:.2f}'.format(te))
