#include<stdio.h>
int main()
{
    int a=20,b=2,w;
    float d;

    printf("Distance: ");
    scanf("%f",&d);
    printf("Waiting Time: ");
    scanf("%d",&w);

    float amount = d*a;
    int waiting = b*w;
    float total = amount + waiting;

    printf("Distance Fare = %.2f\n",amount);
    printf("Waiting Fare = %d\n",waiting);
    printf("Total Fare = %.2f\n",total);
}
