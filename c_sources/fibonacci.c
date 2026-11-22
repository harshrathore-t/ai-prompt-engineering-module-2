#include <stdio.h>
void fibonacci(int n) {
    if (n < 0 || n > 20) return;
    int a = 0, b = 1;
    for (int i = 0; i < n; ++i) {
        printf("%d%s", a, i == n - 1 ? "\n" : " ");
        int next = a + b;
        a = b;
        b = next;
    }
}
int main(void) {
    fibonacci(7);
    return 0;
}
