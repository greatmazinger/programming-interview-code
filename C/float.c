#include <stdio.h>
#include <math.h>
#include <stdbool.h>

// Floating point questions in C.

bool add_and_test(float a, float b)
{
    if ((a == 0.0) || (b == 0.0)) {
        return 0;
    }
    return ((a + b) == a);
}

bool sub_and_test(float a, float b)
{
    if ((a == 0.0) || (b == 0.0)) {
        return 0;
    }
    return ((a - b) == a);
}

int main()
{
    float a = INFINITY;
    float b = INFINITY;
    float aNan = NAN;
    float bNan = NAN;
    float negZero = -0.0;
    float zeroExp = 0.0E126;
    printf("Inf + Inf == Inf ? %d\n", add_and_test(a, b));
    printf("Inf + small number == Inf ? %d\n", add_and_test(a, 0.0000000001));
    printf("5.0 + -0.0 == 5.0 ? %d\n", add_and_test(5.0, negZero));
    printf("Inf - Inf == Inf ? %d\n", sub_and_test(a, b));
    printf("Inf - Inf == 0 ? %d\n", (a - b) == 0.0);
    printf("Inf - Inf == %f\n", a - b);
    printf("nan + nan == nan ? %d\n", add_and_test(aNan, bNan));
    printf("0.0 == -0.0 ? %d\n", 0.0 == -0.0);
    printf("0.0 == -0.0 ? %d\n", 0.0 == zeroExp);
}
