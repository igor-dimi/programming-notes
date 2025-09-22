#include <stdio.h>
#include <stdarg.h>


void mysum(int count, ...) {
    va_list args;
    va_start(args, count);

    int total = 0;
    for (int i = 0; i < count; i++) total += va_arg(args, int);

    va_end(args);
    printf("Sum = %d\n", total);
}

int main(int argc, char const *argv[])
{
    mysum(3, 10, 20, 30);
    return 0;
}


