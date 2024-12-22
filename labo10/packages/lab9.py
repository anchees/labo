def generator(pos1, pos2):
    pos1=set(pos1)
    pos2=set(pos2)
    for i in pos1:
        for j in pos2:
            result=i+j
            yield result

