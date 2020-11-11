#utf-8
import nltk
from nltk import *
import re
f1=open('D:\\vue-projects\\segment_v1.0\\server\\api\\file\\sentiment.txt','r',encoding='utf-8')
f2=open('D:\\vue-projects\\segment_v1.0\\server\\api\\file\\res_label.data','w',encoding='utf-8')
f3=open('D:\\vue-projects\\segment_v1.0\\server\\api\\file\\dictionary.txt','r',encoding='utf-8')
text=f1.read()
dictionary=f3.read()
words=dictionary.split('\n')
reg_parser=RegexpParser(''' 
       NP:{<DT>?<JJ|JJR|JJS>*<NN|NNS|NNP|NNPS>*}
        P:{<IN>}
        PP:{<P> <NP>}
        VP:{<VB|VBD|VBG|VBN|VBP|VBZ> <NP|PP>*}
        ''')
def pos_simpleify (i):
    pos=i[1]
    if i[1].startswith('NN'):
        pos='NN'
    elif i[1].startswith('JJ'):
        pos='JJ'
    elif i[1].startswith('RB'):
        pos='RB'
    elif i[1].startswith('VB'):
        pos='VB'
    return pos
def get_features(i):
    s=''
    if type(i)==tuple:
        pos=pos_simpleify(i)
        if((i[0]+' ').lower() in words):
            s=i[0]+' '+pos+' '+'Y'+' '+'OP'+' '+'C'
        else:
            if (i[0].isupper()==True):
                s=i[0].lower()+' '+pos+' '+'N'+' '+'OP'+' '+'T'
            else:
                s=i[0]+' '+pos+' '+'N'+' '+'OP'+' '+'O'
        f2.write(s+'\n')
    else:
        lab=i.label()
        for j in i:
            if type(j)==tuple:
                pos=pos_simpleify(j)
                if((j[0]+' ').lower() in words):
                    s=j[0]+' '+pos+' '+'Y'+' '+lab+' '+'C'
                else:
                    if (j[0].isupper()==True):
                        s=j[0].lower()+' '+pos+' '+'N'+' '+lab+' '+'T'
                    else:
                        s=j[0]+' '+pos+' '+'N'+' '+lab+' '+'O'
                f2.write(s+'\n')
            else:
                get_features(j)
english_punctuations=['.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','\"','\'',"''",'""','-',' ']
i=0
for sent in nltk.sent_tokenize(text):
    text_list=nltk.word_tokenize(sent)
    text_list=[word for word in text_list if word not in english_punctuations]
    text_list=nltk.pos_tag(text_list)
    t=reg_parser.parse(text_list)
    for i in t:
        get_features(i)
    f2.write('\n')
f1.close()
f2.close()
f3.close()
