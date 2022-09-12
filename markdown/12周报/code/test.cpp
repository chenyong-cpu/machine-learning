#include <iostream>
#include <string>

using namespace std;

int main(int argc, char const *argv[])
{
    string str = "12343";

    int i = 0;

    cout << str.substr(0, i) + str.substr(i + 1, str.length()) << endl;
    
    return 0;
}
