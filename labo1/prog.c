#include <stdio.h> 

int main(){
    int x,y,z;  
    printf("Enter x -> ");
    scanf("%d", &x);   
    printf("Enter y -> ");
    scanf("%d", &y);  
    printf("Enter z -> ");
    scanf("%d", &z);
        int max = x>y && x>z? x : y>z && y>x? y : z, sum = x>y && x>z? y+z : y>z && y>x? x+z : x+y;
    if (max>sum)
        printf("%d\n", max);
    else
        printf("%d\n", sum-max);
    // if (x>y && x>z) {
    //     int s=y+z;
    //     if (x>s)
    //         printf("%d\n", x);
    //     else
    //         printf("%d\n", s-x);
    // } else if (y>x && y>z){
    //     int s=x+z;
    //     if (y>s)
    //         printf("%d\n", y);
    //     else
    //         printf("%d\n", s-y);
    // } else if (z>x && z>y){
    //     int s=x+y;
    //     if (z>s)
    //         printf("%d\n", z);
    //     else
    //         printf("%d\n", s-z);
    // } else 
    //     printf("неприавльные значения\n");
    return 0;
}