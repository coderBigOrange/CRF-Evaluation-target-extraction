f1=open('result_lap_8.txt','r',encoding='UTF-8')
TP_t=0
TN_t=0
FP_t=0
FN_t=0
TP_c=0
TN_c=0
FP_c=0
FN_c=0
while True:
    line=f1.readline()
    if not line:
        break
    elif line=='\n':
        continue
    else:
        line.replace('\n','')
        list=line.split('\t')
        list[5]=(list[5].split('\n'))[0]
        if list[4]==list[5]:
            if list[4]=='T':
                TP_t+=1
                TN_c+=1
            elif list[4]=='C':
                TP_c+=1
                TN_t+=1
            else:
                TN_c+=1
                TN_t+=1
        else:
            if list[4]=='T':
                FN_t+=1
                if list[5]=='C':
                    FP_c+=1
                else:
                    TN_c+=1
            elif list[4]=='C':
                FN_c+=1
                if list[5]=='T':
                    FP_t+=1
                else:
                    TN_t+=1
            else:
                if list[5]=='T':
                    FP_t+=1
                    TN_c+=1
                else:
                    FP_c+=1
                    TN_t+=1
accuracy_t=(TP_t+TN_t)/(TP_t+TN_t+FP_t+FN_t)
accuracy_c=(TP_c+TN_c)/(TP_c+TN_c+FP_c+FN_c)
precision_t=TP_t/(TP_t+FP_t)
precision_c=TP_c/(TP_c+FP_c)
recall_t=TP_t/(TP_t+FN_t)
recall_c=TP_c/(TP_c+FN_c)
Ft=2*TP_t/(2*TP_t+FP_t+FN_t)
Fc=2*TP_c/(2*TP_c+FP_c+FN_c)
print('抽取对象： 准确率=%f,精确率=%f,召回率=%f,F值=%f'%(accuracy_t,precision_t,recall_t,Ft))
print('抽取评论： 准确率=%f,精确率=%f,召回率=%f,F值=%f'%(accuracy_c,precision_c,recall_c,Fc))
            
        

            
            
