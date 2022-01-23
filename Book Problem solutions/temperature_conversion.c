/*TEMPERATURE CONVERSION*/
#include<stdio.h>
#define F_Low 0   /* ------------------ */
#define F_Max 250 /* SYMBOLIC CONSTANTS */
#define STEP 25   /* ------------------ */
int main()
{

    typedef float REAL;            /* TYPE DEFINITION */
    REAL fahrenheit,celsius;       /* DECLARATION */

    fahrenheit = F_Low;     /* INITIALIZATION */

    printf("Fahrenheit Celsius\n\n");
    while (fahrenheit <= F_Max)
    {
        celsius = (fahrenheit - 32.0) / 1.8;
        printf(" %5.1f %7.2f\n ", fahrenheit,celsius);
        fahrenheit = fahrenheit + STEP;

    }

    return 0;
}
