#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <string.h>

using namespace std;

int n;
int answer = INT_MAX;
int board[16][16];
int dp[16][1 << 16];

int dfs(int cur, int visited)
{
    if (visited == (1 << n) - 1)
    {
        if (board[cur][0] == 0)
            return 1e9;
        else
            return board[cur][0];
    }
    if (dp[cur][visited] != -1)
        return dp[cur][visited];
    dp[cur][visited] = 1e9;

    for (int next = 0; next < n; next++)
    {
        if (board[cur][next] == 0)
            continue;
        if ((visited & (1 << next)) == 1 << next)
            continue;
        dp[cur][visited] = min(dp[cur][visited], board[cur][next] + dfs(next, visited | 1 << next));
    }
    return dp[cur][visited];
}

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cin >> board[i][j];
    }
    memset(dp, -1, sizeof(dp));
    
    cout << dfs(0, 1);
    // cout << answer;
}