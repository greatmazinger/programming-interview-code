#include <iostream>
int main()
{
    int &r = *(new int(100));
    std::cout << r << std::endl;
    return 0;
}
