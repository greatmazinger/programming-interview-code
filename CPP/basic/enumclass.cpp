#include <iostream>


enum class ECTest {
    One = 1,
    Two = 2,
    Three = 3
};


int main( int argc, char *argv[] )
{
    using std::cout;
    using std::endl;

    ECTest e1 = ECTest::One;
    ECTest eone = ECTest::One;
    ECTest e2 = ECTest::Two;
    ECTest e3 = ECTest::Three;

    if (e1 == eone) {
        cout << "== is OK." << endl;
    } else {
        cout << "ERROR: e1 != eone" << endl;
    }

    cout << "===============================================================================" << endl;
    switch (e2) {
        case ECTest::One:
            cout << "One." << endl;
            break;
        case ECTest::Two:
            cout << "Two." << endl;
            break;
        case ECTest::Three:
            cout << "Three." << endl;
            break;
        default:
            cout << "ERROR: DEFAULT." << endl;
            break;
    }
}
