#include <stdio.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int main(){
    double h;
    FILE *graph;
    printf("Enter h: ");
    scanf("%lf", &h);
    graph = fopen("graph.txt", "w");
    for (double x=-1; x<=2+(h/2) ; x=x+h){
        if (x<=1){
            fprintf(graph, "%.6lf\t%.6lf\n", x, exp(-2*sin(x)));
            printf("%.6lf\t%.6lf\n", x, exp(-2*sin(x)));
        } else{
            fprintf(graph, "%.6lf\t%.6lf\n", x, pow(x,2)-cos(x)/sin(x));
            printf("%.6lf\t%.6lf\n", x, pow(x,2)-cos(x)/sin(x));
        }
    }
    fclose(graph);
    FILE *gnuplotPipe = fopen("test.gnu", "w");
    fprintf(gnuplotPipe, "set term gif \\\n");
    fprintf(gnuplotPipe, "    animate \\\n");
    fprintf(gnuplotPipe, "    optimize \\\n");
    fprintf(gnuplotPipe, "    delay 150 \\\n");
    fprintf(gnuplotPipe, "    size 300, 300 \\\n");
    fprintf(gnuplotPipe, "    background \"#ffeedf\" \\\n");
    fprintf(gnuplotPipe, "    crop \n");
    fprintf(gnuplotPipe, "set output \"hohoho.gif\"\n");
    fprintf(gnuplotPipe, "set xlabel \"x\"\n");
    fprintf(gnuplotPipe, "set ylabel \"f(x)\"\n");
    fprintf(gnuplotPipe, "set grid\n");
    fprintf(gnuplotPipe, "set title \"График функции f(x)\"\n");
    fprintf(gnuplotPipe, "do for [i=0:3]{\n");
    fprintf(gnuplotPipe, "    plot \"graph.txt\" with lines title \"f(x)\" \n");
    fprintf(gnuplotPipe, "    plot \"graph.txt\" with points title \"f(x)\"\n");
    fprintf(gnuplotPipe, "    plot \"graph.txt\" with boxes title \"f(x)\"\n}");
    fclose(gnuplotPipe);
    system("gnuplot test.gnu");
// set terminal png enhanced
// set output 'graphimage.png'
// set xlabel "x" 
// set ylabel "f(x)"
// set grid
// set title "График функции f(x)"

// plot "graph.txt" with lines title "f(x)"
    return 0;
}