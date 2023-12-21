#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

vector<int> chu;
char dp[30][40001];

int main()
{
    int n;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;

        cin >> temp;
        chu.push_back(temp);
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j < 40001; j++)
        {
            if (chu[i] == j)
                dp[i][j] = 'Y';
            else if (i == 0)
                dp[i][j] = 'N';
            else if (i > 0 && dp[i - 1][j] == 'Y')
                dp[i][j] = 'Y';
            else if (chu[i] - j > 0 && dp[i - 1][chu[i] - j] == 'Y')
                dp[i][j] = 'Y';
            else if (j - chu[i] > 0 && dp[i - 1][j - chu[i]] == 'Y')
                dp[i][j] = 'Y';
            else if (dp[i - 1][chu[i] + j] == 'Y')
                dp[i][j] = 'Y';
            else
                dp[i][j] = 'N';
        }
    }
    
    int m;

    cin >> m;
    for (int i = 0; i < m; i++)
    {
        int ball;

        cin >> ball;
        cout << dp[n - 1][ball] << " ";
    }
}