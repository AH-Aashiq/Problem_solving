/* Convert Days into Month  */
#include<stdio.h>
int main()
{
    int month, days;   /* VARIABLES */
    printf("\nEnter days: ");
    scanf("%d",&days);

    month = days / 30;
    printf("Months = %d Days = %d", month,days); /* FINAL RESULT PRINT */


    return 0;

}
