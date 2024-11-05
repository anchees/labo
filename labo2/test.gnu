set term gif \
    animate \
    optimize \
    delay 150 \
    size 300, 300 \
    background "#ffeedf" \
    crop 
set output "hohoho.gif"
set xlabel "x"
set ylabel "f(x)"
set grid
set title "График функции f(x)"
do for [i=0:3]{
    plot "graph.txt" with lines title "f(x)" 
    plot "graph.txt" with points title "f(x)"
    plot "graph.txt" with boxes title "f(x)"
}