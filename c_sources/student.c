#include <stdio.h>
struct Student {
    char roll[16];
    char name[40];
    float marks;
};
int main(void) {
    struct Student s = {"472", "Harshvardhan Singh", 85.5f};
    printf("%s %s %.1f\n", s.roll, s.name, s.marks);
    return 0;
}
