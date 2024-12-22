#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1,"bear")
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
for i in birds:
    zoo.append(i)
print(zoo)

# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo.__delitem__(3)
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
for i in zoo:
    if i=="lion":
        print("Лев сидит в клетке №",zoo.index(i)+1)
    elif i=="lark":
        print("Жаворонок сидит в клетке №",zoo.index(i)+1)
