#include <iostream>
#include <iomanip>
#include <cstdio>
using namespace std;

int main() {
    // Complete the code.
    int a;
    long b;
    char c;
    float d;
    double e;
    scanf("%d %ld %c %f %lf", &a, &b, &c, &d, &e);
    std::cout
       << a << endl
       << b << endl
       << c << endl;
    std::setw(3);
    std::setprecision(3);
    std::cout << std::fixed << d << endl;
    std::setw(9);
    std::setprecision(9);
    std::cout << std::fixed << e << endl;
    return 0;
}
