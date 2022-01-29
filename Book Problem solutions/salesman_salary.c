/*------ Salesman's Salary---*/
/*--A computer manufacturing company has the following

monthly compensation policy to their sales-persons:

Minimum base salary                             : 1500.00
Bonus for every computer sold                   :  200.00
Commission on the total monthly sales           :  2 per cent(2%)

Since the prices of computers are changing the sales price of each computer
is fixed at the beginning of every month.
A program to compute a sales person's gross salary is given bellow :
*/

#include<stdio.h>
#define BASE_SALARY 1500.00
#define BONUS_RATE 200.00
#define COMMISSION 0.02

int main()
{
    int quantity;
    float gross_salary, price;
    float bonus,commission ;
    printf("Input number sold and price\n");
    scanf("%d %f",&quantity,&price);

    bonus = BONUS_RATE * quantity;
    commission = COMMISSION * quantity * price;
    gross_salary = BASE_SALARY + bonus + commission;

    printf("\n");

    printf("Bonus = %6.2f\n",bonus);
    printf("Commission = %6.2f\n",commission);
    printf("Gross salary = %6.2f\n",gross_salary);

}

