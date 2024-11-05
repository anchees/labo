# Лабораторная работа №2 | 7-ой вариант
## Задание
1) Напишите программу по варианту, используя оператор цикла ``while`` (нечётные варианты) или ``do while`` (чётные варианты).
2) Напишите программу, используя оператор цикла ``for``.
3) Постройте график с использованием gnuplot.
4) Составьте блок-схемы.
5) формите отчёт в README.md. Отчёт должен содержать:
- Задание
- Описание проделанной работы
- Скриншоты результатов
- Блок-схемы
- График функции
- Ссылки на используемые материалы

### Задание варианта:
$$
f(x) =
  \begin{cases}
    e^{-2sin x} \text{,}       & -1 \leq x \leq 1 \text{;} \\
    x^2 - ctg x \text{,} & 1 < x \leq 2 \text{.}
  \end{cases}
$$



## Описание проделанной работы
- Написал код с циклом ``while``:
![whilecode](whilecode.png)
- Также написал код с циклом ``for``:
![forcode](forcode.png)
- Установил **gnuplot**, добавил его как среду разроботки **windows** и скачал расширения в **VSC**
- Создал текстовый файл для сохранения вывода
- Сделал график с помощью команды ``gnuplot graphs.gnu``
- Сделал отсчет


## Скриншоты результатов 
### Цикл ``while``:
- В командной строке:
![resultwhile](comandwhile.png)
- В текстовом документе:
![resulttxtfor](txtwhile.png)
### Цикл ``for`` :
- В командной строке:
![resultfor](comandfor.png)
- В текстовом документе:
![resulttxtwhile](txtfor.png)



## Блок схемы
### Для цикла ``while``:
![№1](blockshem1-1.png)
### Для цикла ``for``:
![№2](blockshema2-1.png)



## График функции
![graphik](graphforreadme-1.png)


## Ссылки на используемые материалы
- https://stackoverflow.com/questions/74930588/gnuplot-setup-vs-code/79056576#79056576 
- https://stackoverflow.com/questions/22615251/gnuplot-bad-data-on-line-1
- https://younglinux.info/c/fopen
- https://codelessons.dev/ru/fprintf-in-c-cplusplus/
- https://habr.com/ru/companies/ruvds/articles/517450/
- https://www.youtube.com/watch?v=mYBr-Yb70Z4&ab_channel=oxyscbw
