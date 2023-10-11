/*
Martina García
This programs prints the absolute value of sin(x) over an interval
14/02/2023
*/

#include<stdio.h>
#include<math.h> // If compiled with gcc, include -lm flag

int main(void)  { 
double interval = 0.0;
for(int i = 0; i <30; i++)  {
    interval = i/10.0;
    printf("sin(%.1lf) = %.3lf \t", interval, fabs(sin(interval)));
    }
printf("\n+++++++\n");
}