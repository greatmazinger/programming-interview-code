#include <iostream>
#include <string>
#include <map>
#include <utility>

int main( int argc, char *argv[] )
{
    using std::cout;
    using std::endl;
    using std::string;
    using std::map;
    using std::pair;

    string one( "First string" );
    string other1( "First string" );
    string two( "Two" );
    string three( "Three" );

    if (one == other1) {
        cout << "== as expected." << endl;
    } else {
        cout << "== NOT working." << endl;
    }

    cout << "================================================================================" << endl;

    typedef pair<string, string> StrPair;
    typedef map< StrPair, int > StrPair2Int;

    StrPair p1 = std::make_pair( one, two );
    StrPair p2 = std::make_pair( one, two );
    StrPair p3 = std::make_pair( three, one );

    StrPair2Int mymap;

    mymap[p1] = 1;
    auto it = mymap.find( p1 );
    if (it != mymap.end()) {
        cout << "Map works as expected on first assign." << endl;
        cout << "  (" << it->first.first << ", " << it->first.second << ") ->  " << it->second << endl;
        mymap[p1] = 100;
    } else {
        cout << "Map DOES NOT work as expected on first assign." << endl;
    }
    
    cout << "================================================================================" << endl;

    cout << "Expecting 100..." << endl;
    cout << mymap[p2] << endl;

    cout << "================================================================================" << endl;

    it = mymap.find( p3 );
    if (it == mymap.end()) {
        cout << "Map works: didn't find string we haven't put it." << endl;
        mymap[p3] = 999;
    } else {
        cout << "Map DOES NOT work as expected on searching for non-existent key." << endl;
    }
    
    cout << "================================================================================" << endl;

    cout << "Expecting 999..." << endl;
    cout << mymap[p3] << endl;

    cout << "================================================================================" << endl;
}
