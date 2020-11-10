#from googletrans import Translator
from collections import Counter 
import json

#translator = Translator()
eng=[]
fr=[]
both=[]
handEng = open('eng.txt')
handFr = open('fr.txt', encoding='utf-8')

#eng
for line in handEng:
    line = line.rstrip()
    eng.append(line) 
    eng = list(dict.fromkeys(eng))
#print(len(eng))
#for i in eng:
#    print(i)

#Fr
for line in handFr:
    line = line.rstrip()
    fr.append(line) 
#for i in fr:
#    print(i)

#merge eng and fr
both = list(map(list, zip(eng, fr)))
#print(both)

###########################################################################
list0= both
list= both
#print(list)

l=[]
order=[]
final = []

def freqCommonLetters(w1, w2):
    w1=w1.lower()
    w2=w2.lower()
    if w1==w2: 
        return 1
    elif (w1 in w2) or (w2 in w1):
        return 0.99999999
    else:
        a = Counter(w1)
        b = Counter(w2)
        return sum(min(a[key], b[key]) for key in a)/max(len(w1),len(w2))

for i in range(len(list)):
    l.append([freqCommonLetters(list[i][0], list[i][1]),i])
print(l)
l.sort(reverse = True)
#print(l)


for i in range(len(l)):
    order.append(l[i][1])
#print(order)  #order of each index


for i in range(len(order)):
    final.append(list0[order[i]])
#print(final)
#for i in final:
#    print(i[1])

#dic =	{}
#for i in range(0,len(final)):
#dic[i] = (final[i][0],final[i][1])
    #dic[i] = { 'eng': final[i][0], 'fr': final[i][1] } 
    #dic[]= { 'eng':final[i][0],'fr': final[i][1] } 
    #dic[final[i][0]]=final[i][1]

dic = []
case=[]
for i in range(0,len(final)):
    case = {'eng':final[i][0], 'fr': final[i][1] }
    dic.append(case)
#print(dic)

#j = json.dumps(dic)
#with open('dic.json', 'w') as f:
#	f.write(j)
#	f.close()