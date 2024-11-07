#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for s1 in sites:
    distances[s1]={}
    for s2 in sites:
        if s1==s2:
            continue
        x1, y1 = sites[s1]
        x2, y2 =sites[s2]
        dist=((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances[s1][s2]=dist

print(distances)




