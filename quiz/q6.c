#include<stdio.h>
int main()
{
    int book,choice;
    printf("Number of books: ");
    scanf("%d",&book);

    printf("Choice one:\n");
    printf("1.Chocolate\n");
    printf("2.Gum\n");

    printf("Choice Your Number between Chocolate and Gum: ");
    scanf("%d",&choice);

    if(choice == 1)
    {
        int c = 3;
        int chocolate = book/c;
        printf("%d",chocolate);

        printf("Number of chocolate is = %d\n",chocolate);

        int gum = book%c;
        printf("Number of gum is = %d\n",gum);

    }
    else
    {
        printf("Number of gum is = %d",book);
    }
}
