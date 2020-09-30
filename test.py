f1=open('res_m_5_all_label.txt','r',encoding='UTF-8')
f2=open('正面评价词语（英文）.txt','r',encoding='UTF-8')
f3=open('负面评价词语(英文).txt','r',encoding='UTF-8')
text_p=f2.read()
text_n=f3.read()
p_words=text_p.split('\n')
n_words=text_n.split('\n')
t='null'
c='null'
while True:
    line=f1.readline()
    if not line:
        break
    elif line=='\n':
        print('term: '+t+'\t'+'polarity: '+c)
        t='null'
        c='null'
    else:
        list=line.split('\t')
        list[5]=(list[5].split('\n'))[0]
        if list[5]=='T':
            if t=='null':
                t=list[0]+' '
            else:
                t=t+list[0]+' '
        elif list[5]=='C':
            if((list[0]+' ').lower() in p_words):
                c='positive'
            elif((list[0]+' ').lower() in n_words):
                c='negtive'
        if list[0]==','and(t!='null'or c!='null'):
            print('term: '+t+'\t'+'polarity: '+c)
            t='null'
            c='null'
f1.close()
f2.close()
f3.close()
            
