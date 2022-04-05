#include <stdio.h>


int main() {
    int a = 0,c  = 0, b = 1, N;
    printf("Enter the length of fibonacci Series: ");
    scanf("%d", &N);
    for (int i = 0; i<N; i++) {
        printf("%d ", c);
        a = b;
        b = c;
        c = a+b;
    }
    printf("\n");
}