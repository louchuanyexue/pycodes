import time
ls=input().split(',')
start=time.mktime(time.strptime(ls[0],"%Y年%m月%d日%H点%M分%S秒"))
end=time.mktime(time.strptime(ls[1],"%Y年%m月%d日%H点%M分%S秒"))
print(int(abs((end-start)//86400)))

