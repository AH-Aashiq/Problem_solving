/* C Program to Print Even Numbers
from 1 to N using For Loop and If */
#include<stdio.h>

int main()
{
    while(1)
    {
        int number;

        printf("\n Please Enter the Maximum Limit Value : ");
        scanf("%d", &number);

        printf("\n Even Numbers between 1 to %d are : \n", number);
        for(int i = 1; i <= number; i++)
        {
            if (i % 2 == 0 )
            {
                printf(" %d \t", i);
            }
        }

    }

    return 0;
}
