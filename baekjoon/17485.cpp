#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
#include <string.h>

using namespace std;

int n, m;
// vector<vector<vector<int> > > board(n, vector<vector<int> >(m, vector<int>(3, INT_MAX)));


int main()
{
    int dp[1000][3];
    
    cin >> n >> m;
    for (int i = 0; i < m; i++)
    {
        int temp;
        cin >> temp;
        for (int k = 0; k < 3; k++)
            dp[i][k] = temp;
    }
    for (int i = 1; i < n; i++)
    {
        int newDp[1000][3];
        for (int j = 0; j < m; j++)
        {
            int temp;
            cin >> temp;
            if (j == 0)
            {
                newDp[j][0] = INT_MAX;
                newDp[j][1] = min(dp[j][0], dp[j][2]) + temp;
                newDp[j][2] = min(dp[j + 1][0], dp[j + 1][1]) + temp;
            }
            else if (j == m - 1)
            {
                newDp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + temp;
                newDp[j][1] = min(dp[j][0], dp[j][2]) + temp;
                newDp[j][2] = INT_MAX;
            }
            else
            {
                newDp[j][0] = min(dp[j - 1][1], dp[j - 1][2]) + temp;
                newDp[j][1] = min(dp[j][0], dp[j][2]) + temp;
                newDp[j][2] = min(dp[j + 1][0], dp[j + 1][1]) + temp;
            }
        }
        memcpy(dp, newDp, sizeof(newDp));
    }
    int ret = INT_MAX;
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < 3; j++)
        {
            // cout << dp[i][j] << " ";
            ret = min(ret, dp[i][j]);
        }
        // cout << "\n";
    }
    cout << ret;
}