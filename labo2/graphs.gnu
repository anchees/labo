#!/usr/bin/env -S gnuplot -persist
set terminal png enhanced
set output 'graphimage.png'
set xlabel "x" 
set ylabel "f(x)"
set grid
set title "График функции f(x)"

plot "graph.txt" with lines title "f(x)"