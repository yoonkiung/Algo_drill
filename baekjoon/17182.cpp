#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

int n, k;
int arr[10][10];
int dp[10][1 << 10];

int dfs(int cur, int visited)
{
    if (visited == (1 << n) - 1)
        return 0;

    if (dp[cur][visited] != -1)
        return dp[cur][visited];
    dp[cur][visited] = 1e9;
    for (int i = 0; i < n; i++)
    {
        if (cur == i)
            continue;
        dp[cur][visited] = min(dp[cur][visited], dfs(i, visited | (1 << i)) + arr[cur][i]);
    }
    return dp[cur][visited];
}

int main()
{
    cin >> n >> k;
    memset(dp, -1, sizeof(dp));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cin >> arr[i][j];
    }

    for (int middle = 0; middle < n; middle++)
    {
        for (int start = 0; start < n; start++)
        {
            for (int end = 0; end < n; end++)
            {
                if (arr[start][end] > arr[start][middle] + arr[middle][end])               
                    arr[start][end] = arr[start][middle] + arr[middle][end];
            }
        }
    }

    cout << dfs(k, 1 << k);
}