#include<stdio.h>

/* int main(void)
{   
    printf("hello world\n");
    return 0;
}

int main(void)
{   
    printf("Una noche\nuna noche toda llena de perfumes, de murmullos y de musica de alas,\nUna noche\nen que ardian en la sombra nupcial y humeda, las luciernagas fantasticas,\na mi lado, lentamente, contra mi cenida, toda,\nmuda y palida\ncomo si un presentimiento de amarguras infinitas,\nhasta el fondo mas secreto de tus fibras te agitara,\npor la senda que atraviesa la llanura florecida\ncaminabas,\ny la luna llena\npor los cielos azulosos, infinitos y profundos esparcia su luz blanca,\ny tu sombra\nfina y langida\ny mi sombra\npor los rayos de la luna proyectada\nsobre las arenas tristes\nde la senda se juntaban.\nY eran una\ny eran una\n¡y eran una sola sombra larga!\n¡y eran una sola sombra larga!\n¡y eran una sola sombra larga!\n");
    return 0;
} 

int main(void) {
    int  miles = 26, yards = 385;
    int kilometers;
    kilometers = 1.609 * (miles + yards/1760.0);
    printf("\nA marathon is %lf kilometers.\n", kilometers);
    return 0;
 }

int main(void)  {
    int a = 3, b = 4, c = -2;
    int res = ++a + b++;
    printf(res);
    return 0;
}*/

#define PI 3.14159
int main(void)
{ 
 double radius;
 printf("Enter radius:");
 scanf("%g", &radius);
 printf(radius);
 printf("volume is : %g \n\n", 4*radius*radius*radius/3 );
return 0;
}