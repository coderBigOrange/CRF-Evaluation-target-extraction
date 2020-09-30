import re
f1=open('orignal_laptops','r',encoding='UTF-8')
f2=open('laptop_normolize.txt','w',encoding='utf-8')
while True:
    line=f1.readline()
    if not line:
        break
    elif line.find('<text>')!=-1:
        text=(re.findall(r">(.+?)<",line))
        sent=text[0]
        sent=sent.lower()
    elif line.find('term=')!=-1:
        ft=re.findall(r"\"(\d+)\"",line,re.M)
        f=int(ft[0])
        t=int(ft[1])
        term=(sent[f:t].upper())
        sent=sent[:f]+term+sent[t:]
        tag=True
    elif line.find('</sentence>')!=-1 and tag==True:
        f2.write(sent+'\n')
        tag=False
f1.close()
f2.close()
