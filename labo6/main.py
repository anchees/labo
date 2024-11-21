from itertools import *
def num1():  
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

def num2():
    print(bin(4**2020+2**2017-15)[2:].count('1'))

def num3():
    for i in range(174457, 174505+1):
        d = []
        for j in range(2, i//2 + 1):
            if i % j == 0:
                d.append(j)
            if len(d) > 2:
                break
        if len(d) == 2:
            print(d[0], d[1])

            
print("Задание 1:")
num1()
print("Задание 2:")
num2()
print("Задание 3:")
num3()