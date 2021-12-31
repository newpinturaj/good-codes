#include <stdio.h>
#include <stdlib.h>

void main()
{
    int i, j, n;
    char ask = 'y';

    printf("Enter the size of the pattern: ");
    scanf("%d", &n);
    printf("For yes: y\n");
    printf("For no : n\n");
    printf("Do you need border: ");
    scanf("\n%c" , &ask);
    fflush(stdin);

    for (i = 0 ; i <n ; i++)
    {
        for(j = 0 ; j <n ; j++)
        {
            if (i == j || j == (n-i-1)) printf("*"); // diagonal
            else if (ask == 'y' || ask == 'Y')  // border
            {
                if (i == 0 || j == 0 || i == n -1 || j == n -1) printf("*");
                else printf(" ");
            }
            else printf(" ");


        }
        printf("\n");
    }
    printf("Press any key to exit\n");
    scanf("%c", &ask);
}