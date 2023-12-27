#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

string add(string a, string b)
{
    int i = 0;
    string temp = "";
    char up = 0;

    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());

    while (i < a.size() && i < b.size())
    {
        char l = a[i] - '0';
        char k = b[i] - '0';
        
        if (up + l + k <= 9)
        {
            temp.insert(temp.begin(), up + l + k + '0');
            up = 0;
        }
        else
        {   
            temp.push_back(up + l + k - 10 + '0');
            up = 1;
        }
        i++;
        // cout << temp << "\n";
    }

    while (i < a.size())
    {
        char l = a[i] - '0';

        if (up + l <= 9)
        {
            temp.insert(temp.begin(), up + l + '0');
            up = 0;
        }
        else
        {   
            temp.insert(temp.begin(), up + l - 10 + '0');
            up = 1;
        }
        i++;
        // cout << temp << "\n";
    }

    while (i < b.size())
    {
        char k = b[i] - '0';

        if (up + k <= 9)
        {
            temp.insert(temp.begin(), up + k + '0');
            up = 0;
        }
        else
        {   
            temp.insert(temp.begin(), up + k - 10 + '0');
            up = 1;
        }
        i++;
        // cout << temp << "\n";
    }

    if (up)
        temp.insert(temp.begin(), '1');
    // cout << "\n";
    return temp;
}

int main()
{
    string dp[251];

    dp[0] = "1";
    dp[1] = "1";
    
    for (int i = 2; i < 251; i++)
    {
        string a = dp[i - 1];
        string b = dp[i - 2];
        dp[i] = add(add(a, b), b);
    }

    while (1)
    {
        int n;

        cin >> n;
        if (cin.eof())
            break;
        cout << dp[n] << "\n";
    }
}