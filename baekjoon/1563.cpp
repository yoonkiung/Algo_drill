#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
#include <string.h>

using namespace std;

int main()
{
    long long n;
    cin >> n;

    vector<vector<long long> > dp(2, vector<long long>(5, 0));
    
    dp[0][0] = 1;
    dp[0][1] = 0;
    dp[0][2] = 1;
    dp[0][3] = 1;
    dp[0][4] = 0;

    dp[1][0] = 2;
    dp[1][1] = 1;
    dp[1][2] = 2;
    dp[1][3] = 2;
    dp[1][4] = 1;

    for (int i = 0; i < n - 2; i++)
    {
        vector<long long> temp(5, 0);
        
        temp[0] = (dp[1][0] + dp[1][3]) % 1000000;
        temp[1] = (dp[1][1] + dp[1][2] + dp[1][4]) % 1000000;
        temp[2] = (dp[1][0] + dp[1][3]) % 1000000;
        temp[3] = (dp[1][0] + dp[1][3] - dp[0][3]) % 1000000;
        temp[4] = (dp[1][1] + dp[1][2] + dp[1][4] - dp[0][4]) % 1000000;

        dp.push_back(temp);
        dp.erase(dp.begin());
    }
    long long ret = 0;
    for (int i = 0; i < 5; i++)
    {
        ret += dp[1][i];
        ret %= 1000000;
    }
        
    cout << ret;
}