f=open(r"C:\Users\15203\Desktop\ce\data.csv",'w+',encoding='utf-8-sig')
ls=[]
la=[]
for line in f:
    line = line.replace("\n","")
    line = line.replace(" ","")
    ls.append(line.split(","))
for i in range(7):
    for item in ls:
        la.append(item[i])
        la.reverse()
    f.write(",".join(la)+'\n')
    la.clear()
f.close()

