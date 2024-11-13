for i in range(174457, 174505+1):
    d = []
    for j in range(2, i//2 + 1):
        if i % j == 0:
            d.append(j)
        if len(d) > 2:
            break
    if len(d) == 2:
        print(d[0], d[1])





                
        