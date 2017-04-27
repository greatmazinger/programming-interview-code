#include <boost/circular_buffer.hpp>
#include <iostream>

#define NUM 3

using namespace std;

int main()
{
    boost::circular_buffer<int> cb(NUM);
    cb.push_back(0);
    cb.push_back(1);
    cb.push_back(2);

    int index = 0;
    cout << "At FULL:" << endl;
    for ( auto iter = cb.begin();
          iter != cb.end();
          iter++ ) {
        cout << "[" << index << "] : " << *iter << " : " << cb[index] << endl;
        index++;
    }
    cout << "==============================================================================" << endl;
    cb.push_back(3);
    cout << "Overwriting once:" << endl;
    index = 0;
    for ( auto iter = cb.begin();
          iter != cb.end();
          iter++ ) {
        cout << "[" << index << "] : " << *iter << " : " << cb[index] << endl;
        index++;
    }
    return 0;
}
