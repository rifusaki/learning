#include <math.h>
#include <stdio.h>

int main(void) {
    double x, sin_x;
    printf("Enter a value between 0 and 1 (non-inclusive): ");
    scanf("%lf", &x);

    // Check if x is in the range (0, 1)
    if (x <= 0 || x >= 1) {
        printf("Error: x must be between 0 and 1 (non-inclusive)\n");
        return 1;
    }

    // Calculate the sine of x
    sin_x = sin(x);

    // Print the result
    printf("The sine of %lf is %lf\n", x, sin_x);

    return 0;
}
