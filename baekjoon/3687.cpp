#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

string big(int n)
{
    string st = "";
    while (n > 0)
    {
        if (n == 3)
        {
             st = '7' + st;
             break;
        }
        st += '1';
        n -= 2;
    }
    // cout << st << "\n";
    return st;
}

string small(int n)
{
    string st = "";

    while (n > 0)
    {
        if (n >= 7 && n - 7 != 1)
        {
            st = '8' + st;
            n -= 7;
        }
        else if (n >= 6 && n - 6 == 0)
        {
            st = '6' + st;
            n -= 6;
        }
        else if (n >= 6 && n - 6 != 1)
        {
            st = '0' + st;
            n -= 6;
        }
        else if (n >= 5 && n - 5 != 1)
        {
            st = '2' + st;
            n -= 5;
        }
        else if (n >= 4 && n - 4 != 1)
        {
            st = '4' + st;
            n -= 4;
        }
        else if (n >= 3 && n - 3 != 1)
        {
            st = '7' + st;
            n -= 3;
        }
        else if (n >= 2 && n - 2 != 1)
        {
            st = '1' + st;
            n -= 2;
        }
        cout << st << " " << n << "\n";
    }
    
    return st;
}


int main()
{
    int t;
    cin >> t;
    while (t > 0)
    {
        int n;
        
        cin >> n;
        cout << small(n) << " " << big(n) << "\n";
        t--;
    }
    
}