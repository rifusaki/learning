/*
Martina García
This programs prints a table of values for sine and cosine between (0, 1)
14/02/2023
*/

#include<stdio.h>
#include<math.h> // If compiled with gcc, include -lm flag

int main(void)  { 

for(double n=0; n<1.01; n+=0.01)    {
    printf("sin(%.2lf) = %.4lf \t cos(%.2lf) = %.4lf \n", n, sin(n), n, cos(n));
}
printf("\n");
return(0);
}