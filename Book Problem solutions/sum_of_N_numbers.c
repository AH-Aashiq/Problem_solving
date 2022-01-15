/*Problem: Write a program to
find the sum of the first N natural numbers
where N would be input by the user.
*/
#include<stdio.h>
int main()
{
    int I,sum,N;
    sum = 0;
    I = 1;

    printf("\nEnter a value for the number N: ");
    scanf("%d",&N);
    while (I <= N)
    {
        sum = sum + I;
        I = I+1;
    }
    printf("The sum is = %d",sum);
}
