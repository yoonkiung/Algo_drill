#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <limits.h>

using namespace std;


long long int n;

int main()
{
    cin >> n;
    
    long long int dp[100001][3];
    dp[1][0] = 1;
    dp[1][1] = 1;
    dp[1][2] = 1;

    for (long long int i = 2; i <= n; i++)
    {
        dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % 9901;
        dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901;
        dp[i][2] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901;
    }

    cout << (dp[n][0] + dp[n][1] + dp[n][2]) % 9901;
}