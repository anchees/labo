def generator(pos1, pos2):
    for i in pos1:
        for j in pos2:
            result=i+j
            yield result

pos=input("введите последоватльность 1: ")
pos1=set(pos)
pos=input("введите последоватльность 2: ")
pos2=set(pos)
otvet=generator(pos1,pos2)
for i in otvet:
    print(i)