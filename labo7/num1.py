def recursion():
    def f(two,one,k,a):
        a.append(f'{one}:{two}')
        if k==two or k==one: return [a]
        return f(one+1,two,k,a[:])+f(one,two+1,k,a[:])
    k=int(input("Введите k "))
    one=0
    two=0
    result=f(one,two,k,[])
    print(result)
    

def norecursion():
    def f(k):
        l=0
        r=len(k)-1
        zap=0
        while(l<r):
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True
    k=(input('ввдите последоватлеьность: '))
    print(f(k))
    k=[1,2,3,2,1]
    print(f(k))


print("С использованием рекусрии (11 вариант):")
recursion()
print("Без использования рекусрии (9 вариант):")
norecursion()