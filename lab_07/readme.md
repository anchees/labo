# Лабораторная работа №7 | Вариант 11/9
## Задание
1) Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
2) Оформите отчёт в README.md. Отчёт должен содержать:
    - Условия задач
    - Описание проделанной работы
    - Скриншоты результатов
    - Ссылки на используемые материалы
### Задание варианта 
1) Функция, возвращающая все возможные результаты спортивных матчей с разницей в ```k```
2) Функция для вычисления
$$
x_i = \frac{x_{i-1} + 1}{x_{i-1} + 2},x_0 = 1.
$$
## Опсиание проделанной работы
### №1
#### **Решение с рекурсией**
``` python
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
```
**Результат:**

![1_1r](images/1_1r.png)

#### **Решение без рекурсии (9 вариант)**
``` python
def norecursion():
    def f(k):
        l=0
        r=len(k)-1
        while(l<r):
            if k[l]!=k[r]:
                return False
            l+=1
            r-=1
        return True
    k=(input("ввдите последоватлеьность: "))
    print(f(k))
    k=[1,2,3,2,1]
    print(f(k))

```
**Результаты:**

![1_2n](images/1_2n.png)
### №2
#### **Решение с рекурсией**
``` python
def recursion():
    def x(i):
        if i==0: return 1
        return (x(i-1)+1)/(x(i-1)+2)
    i=int(input("Введите i "))
    print(x(i))
```
**Результат:**

![2](images/2.png)
#### **Решение без рекурсии**
``` python
def norecursion():
    i=int(input("Введите i "))
    x=1
    if i!=0:
        for a in range(x,i):
            x=(x+1)/(x+2)
    print(x)
```
**Результат:**

![2n](images/2n.png)
