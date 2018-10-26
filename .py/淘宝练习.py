import requests
import re
def Gethtml(url):
    try: 
        r = requests.get(url,timeout = 30)
        r.raise_for_status()
        r.encoding =r. apparent_encoding
        return r.text
    except:
        return ""
def Appenpage(ilt,html):
    try:
        title=re.findall(r'\"raw_title\"\:\".*?\"',html)
        price=re.findall(r'\"view_price\"\:\"[\d\.]*\"',html)
        for i in range(len(title)):
            tlt=eval(title[i].split(":")[1])
            plt=eval(price[i].split(":")[1])
            ilt.append([tlt,plt])
    except:
        print("")
def Printpage(ilt):
    tplt="{:4}\t{:16}\t{:8}"
    print(tplt.format("序号","商品名称","价格"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods = "书包"
    start_url = "https://s.taobao.com/search?q="+goods
    info=[]
    depth = 2
    for i in range(depth):
        try:
            url = start_url+"&s="+str(44*i)
            html=Gethtml(url)
            Appenpage(info,html)
        except:
            continue
    Printpage(info)
main()
