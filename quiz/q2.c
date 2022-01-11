#include<stdio.h>
int main()
{
    while(1)
    {
        int number;
        printf("Enter Integer Number: ");
        scanf("%d",&number);
        if(number%2==0)
        {
            int odd_number = number+1;
            printf("Your Next odd number is = %d\n",odd_number);
        }
        else
        {
            printf("Invalid Input Number");
        }

    }

}
