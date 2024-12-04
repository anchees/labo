def recursion():
    def f(one, two, k, mn):
        mn.add((one, two))
        if one==k or two==k: return 0
        f(one+1, two, k, mn)
        f(one, two+1, k, mn)
    one = 0
    two = 0
    k = int(input("Введите k: "))
    mn = set()
    f(one, two, k, mn)
    print(mn)


def norecursion():
    one=0
    two=0
    result=set()
    k=int(input("Введите k "))
    for one in range (k+1):
        for two in range(k+1):
            if (one==k and two==k):
                continue
            result.add((one,two))
        if (one==k and two==k):
            continue
        result.add((one,two))
    print(result)


print("С использованием рекусрии:")
recursion()
print("Без использования рекусрии:")
norecursion()