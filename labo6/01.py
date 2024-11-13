from itertools import *
name='ТИМОФЕЙ'
comb=product(name, repeat=5)
scet=0
for i in comb:
    if ''.join(i).count('Й')<=1 and\
        i[0]!='Й' and i[4]!='Й' and\
        i[0]+i[1]!='ИЙ' and i[1]+i[2]!='ИЙ' and\
        i[2]+i[3]!='ИЙ' and\
        i[1]+i[2]!='ЙИ' and i[2]+i[3]!='ЙИ' and\
        i[3]+i[4]!='ЙИ':
            scet+=1
print(scet)
