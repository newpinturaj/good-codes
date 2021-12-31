#include <stdio.h>

void main()
{
    int i, j, n;
    printf("What should be the size: ");
    scanf("%d", &n);
        //upper half
    for(i =0; i<n; i++)
    {
        for (j = 0; j<n; j++)
        {
            if (j>=(n-i-1))printf("*");
            else printf(" ");
        }
        printf("\n");
    }
    //lower half
    for(i =0; i<n-1; i++)
    {
        for (j = 0; j<n; j++)
        {
            if (j>i)printf("*");
            else printf(" ");
        }
        printf("\n");
    }


    
}