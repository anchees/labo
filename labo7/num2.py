def recursion():
    def x(i):
        if i==0: return 1
        return (x(i-1)+1)/(x(i-1)+2)
    i=int(input("Введите i "))
    print(x(i))
def norecursion():
    i=int(input("Введите i "))
    x=1
    if i!=0:
        for a in range(x,i):
            x=(x+1)/(x+2)
    print(x)
print("С использованием рекусрии:")
recursion()
print("Без использования рекусрии:")
norecursion()