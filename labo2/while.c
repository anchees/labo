#include <stdio.h>
#include <math.h>

int main(){
    double h, x=-1;
    FILE *graph;
    printf("Enter h: ");
    scanf("%lf", &h);
    graph = fopen("graph.txt", "w");
    while (x<=2){
        if (x<=1){
            fprintf(graph, "%lf\t%lf\n", x, exp(-2*sin(x)));
            printf("%lf\t%lf\n", x, exp(-2*sin(x)));
        } else{
            fprintf(graph, "%lf\t%lf\n", x, pow(x,2)-cos(x)/sin(x));
            printf("%lf\t%lf\n", x, pow(x,2)-cos(x)/sin(x));
        }
        x+=(h/2);
        x=round(x*1000000)/1000000;
    }
    fclose(graph);
    return 0;
}