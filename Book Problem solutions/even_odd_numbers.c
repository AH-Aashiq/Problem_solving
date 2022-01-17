/*C program to check numbers are EVEN or ODD from 1 to N.*/

#include <stdio.h>
/*Function*/
int checkEven(int num)
{
    /*if number (num) is divisible by 2, number is even*/
    if (num % 2 == 0)
        return 1;
    else
        return 0;
}

int main()
{
    int i, n;

    printf("\nEnter the value of N: ");
    scanf("%d", &n);

    for (i = 1; i <= n; i++)
    {
        if (checkEven(i))
            printf("%4d [EVEN]\t", i);
        else
            printf("%4d [ODD]\t", i);
    }

    return 0;
}
