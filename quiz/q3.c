#include<stdio.h>
int main()
{
    int annual_salary;

    printf("Enter your Annual salary: ");
    scanf("%d",&annual_salary);

    float monthly_salary = annual_salary / 12;
    printf("Your monthly salary is = %.2f\n",monthly_salary);

    return 0;

}
