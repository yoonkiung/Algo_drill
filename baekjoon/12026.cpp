#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <limits.h>

using namespace std;


int n;
char s[1001];

int main()
{
    cin >> n >> s;

    int dp[1001][2];
    //  index, visited

    for (int i = 1; i <= n; i++)
    {
        dp[i][0] = INT_MAX;
        dp[i][1] = false;
    }
    dp[1][0] = 0;
    dp[1][1] = true;

    for (int i = 2; i <= n; i++)
    {
        char checkWord;
        if (s[i - 1] == 'B')
            checkWord = 'J';
        else if (s[i - 1] == 'O')
            checkWord = 'B';
        else
            checkWord = 'O';

        for (int j = 1; j < i; j++)
        {
            if (s[j - 1] == checkWord && dp[j][0] != INT_MAX)
                dp[i][0] = min(dp[i][0], dp[j][0] + (i - j) * (i - j));
            if (dp[i][0] != INT_MAX)
                dp[i][1] = true;
        }       
    }
    
    if (dp[n][1])
        cout << dp[n][0];
    else
        cout << -1;
}