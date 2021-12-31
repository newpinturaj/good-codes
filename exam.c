#include <stdio.h>

void main()
{
    int N, i;
    printf("Enter a positive integer: ");
    scanf("%d", &N);
    for(i = 0; i<N; i++)
    {
        if (i %2 == 0 && i > 0)
        printf("%d\n" , i);
    }

}