//Problem: Calculation of Average of N numbers using while loop
#define N 10
main()
{
    int count;
    float sum,average,number;
    sum = 0;
    count = 0;
    while(count < N)
    {
        scanf("%f",&number);
        sum = sum + number;
        count = count + 1;
    }

    average = sum/N;
    printf("N = %d Sum = %f",N,sum);
    printf(" Average = %f",average);
}
