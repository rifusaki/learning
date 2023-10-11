/*
Martina García
This programs prints the value of sin(x) given an input x between (0,1)
31/01/2023
*/

#include<stdio.h>
#include<math.h>

int main(void) {
    double x = 0.0;
    while(1) {
        printf("Input angle (radians): ");
        scanf("%lf", &x);
        if(x>0 && x<1) {break;}
        else {continue;}
    }
    printf("sin(%lf) = %lf \n", x, sin(x)); // If compiled with gcc, include -lm flag
    return 0;
}