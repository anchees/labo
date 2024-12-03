# Лабораторная работа №5 | 7-ой вариант
## Задание 
1) Создайте в каталоге для данной ЛР в своём репозитории виртуальное окружение и установите в него ```matplotlib``` и ```numpy```. Создайте файл ```requirements.txt```.
2) Откройте книгу [1] и выполните уроки 1-3. Первый урок можно начинать со стр. 8.
3) Выберите одну из неразрывных функции своего варианта из лабораторной работы №2, постройте график этой функции и касательную к ней. Добавьте на график заголовок, подписи осей, легенду, сетку, а также аннотацию к точке касания.
4) Добавьте в корень своего репозитория файл .gitignore отсюда, перед тем как делать очередной коммит.
5) Оформите отчёт в README.md. Отчёт должен содержать:
- графики, построенные во время выполнения уроков из книги
- объяснения процесса решения и график по заданию 4
6) Склонируйте этот репозиторий НЕ в ваш репозиторий, а рядом. Изучите использование этого инструмента и создайте pdf-версию своего отчёта из README.md. Добавьте её в репозиторий.

## Работа с виртуальным окружением
1) Скачал "Anaconda"
2) Добавил ее как системную переменную "Windows"
3) В командной строке пропписал команду ```conda create -n myenv python``` для создания виртуального окружения
4) Прописал данную команду ```conda init``` чтобы терминал мог корректно работать с ```conda```
5) Для актвиации виртуального окружения использовал команду ```conda activate myenv```
6) Команды ```conda install numpy``` и ```conda install matplotlib``` для установки библиотек
7) Команда ```conda list --export > requirements.txt``` для переноса данных обо всех установленных бибилиотеках в соответсвующий файл 
(```cat requirements.txt``` для проверки того правильно ли все перенеслось)

## Выполнение уроков
### Урок 1.2
``` python
import matplotlib.pyplot as plt

plt.plot([1,2,3,4,5],[1,2,3,4,5])
plt.show()
```
![1_2](lessons/images/1_2.png)
### Урок 1.3
``` python
import matplotlib.pyplot as plt
import numpy as np

# Независимая (x) и зависимая (y) переменные
x = np.linspace(0, 10, 50)
y = x
# Построение графика
plt.title('Линейная зависимость y = x') # заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y') # ось ординат
plt.grid()      
# включение отображение сетки
plt.plot(x, y)  # построение графика
plt.show()
```
![1_3](lessons/images/1_3.png)
### Урок 1.4
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.title('Зависимость: y1 = x, y2 = x^2') #заголовок
plt.xlabel('x') # ось абсцисс
plt.ylabel('y1, y2') # ось ординат   
plt.grid() # включение отображение сетки
plt.plot(x, y1, x, y2) # построение графика
plt.show()
```
![1_4](lessons/images/1_4.png)

### Урок 1.5
``` python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,10,50)
y1 = x #линейная зависимость
y2 = [i**2 for i in x] #квадратичная зависимость

plt.figure(figsize=(9, 9)) #построение графика
plt.subplot(2, 1, 1)
plt.plot(x, y1) #построение графика            
plt.title('Зависимости: y1 = x, y2 = x^2') #заголовок
plt.ylabel('y1', fontsize=14) #ось ординат
plt.grid(True) #ось ординат    

plt.subplot(2, 1, 2)
plt.plot(x, y2) #gостроение графика         
plt.xlabel('x', fontsize=14) #ось абсцисс   
plt.ylabel('y2', fontsize=14) #ось ординат  
plt.grid(True) #включение отображение сетки                 

plt.show()
```
![1_5](lessons/images/1_5.png)

### Урок 1.6
``` python
import matplotlib.pyplot as plt

fruits = ['apple', 'peach', 'orange', 'bannana', 'melon'] #название фруктов
counts = [34, 25, 43, 31, 17] #количество фруктов
plt.bar(fruits, counts) #построение вертикальной столбчатой диаграммы
plt.title('Fruits!') #заголовок
plt.xlabel('Fruit') #ось абцисс
plt.ylabel('Count') #ось ординат
plt.show()
```
![1_6](lessons/images/1_6.png)
### Урок 2.1 + 2.2
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, label = 'steel price') #по оси ординат (ось y), а по оси абсцисс (ось x) будут отложены индексы элементов массива
plt.xlabel('Day', fontsize=15, color='blue')
plt.title('График', fontsize=17)
plt.ylabel('Price', fontsize=15, color='blue')
plt.legend()
plt.grid(True)
plt.text(15, 4, 'grow up!')
plt.show()
```
![2_1+2](lessons/images/2_1+2.png)
### Урок 2.3
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [1, 7, 3, 5, 11]
plt.plot(x, y, '--r')
plt.show()
```
![2_3](lessons/images/2_3.png)
### Урок 2.4
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
# Настройка размеров подложки
plt.figure(figsize=(12, 7))
plt.subplot(2, 2, 1)
plt.plot(x, y1, '-')
plt.subplot(2, 2, 2)
plt.plot(x, y2, '--')
plt.subplot(2, 2, 3)
plt.plot(x, y3, '-.')
plt.subplot(2, 2, 4)
plt.plot(x, y4, ':')
plt.show()
```
![2_4](lessons/images/2_4.png)
### Урок 2.5
``` python
import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [i*1.2 + 1 for i in y1]
y3 = [i*1.2 + 1 for i in y2]
y4 = [i*1.2 + 1 for i in y3]
plt.plot(x, y1, '-', x, y2, '--', x, y3, '-.', x, y4, ':')
plt.show()
```
![2_5](lessons/images/2_5.png)
### Урок 3.1
``` python
import matplotlib.pyplot as plt

locs = ['best', 'upper right', 'upper left', 'lower left',
'lower right', 'right', 'center left', 'center right',
'lower center', 'upper center', 'center']
x = [1, 5, 10, 15, 20]
y1 = [1, 7, 3, 5, 11]
y2 = [4, 3, 1, 8, 12]
plt.figure(figsize=(12, 12))
for i in range(3):
    for j in range(4):
        if i*4+j < 11:
           plt.subplot(3, 4, i*4+j+1)
           plt.title(locs[i*4+j])
           plt.plot(x, y1, 'o-r', label='line 1')
           plt.plot(x, y2, 'o-.g', label='line 2')
           plt.legend(loc=locs[i*4+j])
        else:
            break
plt.show()
```
![3_1](lessons/images/3_1.png)

## Задание варианта
``` python
import matplotlib.pyplot as plt
import math

ymin=None
xcos=None
cas=[]
x=[]
y=[]
xv = -1
while xv <= 2:
    per=0
    if xv <= 1:
        yv = math.exp(-2 * math.sin(xv))
        if ymin==None:
            ymin=yv
            per=1
        if ymin>yv:
            ymin=yv
            per=1
    else:
        yv = xv**2 - math.cos(xv) / math.sin(xv)
        if ymin>yv:
            ymin=yv
            per=1
    x.append(xv)
    y.append(yv)
    if per==1:
        xcos=xv
    xv += 0.1
    
xv=-1
while xv <= 2:
    cas.append(ymin)   
    xv += 0.1
plt.scatter(xcos, ymin, color='green')
plt.annotate('Точка касания', xy=(xcos, ymin))
plt.plot(x, y)
plt.plot(x,cas,label='касательная')
plt.xlabel('x')
plt.ylabel('y')
plt.title('График функции 7 вариант')
plt.legend()
plt.show()
```
![7v](lessons/images/7v.png)