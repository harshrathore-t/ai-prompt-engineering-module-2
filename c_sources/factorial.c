#include <stdio.h>
long factorial(int n) {
    if (n < 0 || n > 12) return -1;
    long result = 1;
    for (int i = 2; i <= n; ++i) result *= i;
    return result;
}
int main(void) {
    printf("factorial(5) = %ld\n", factorial(5));
    return 0;
}
