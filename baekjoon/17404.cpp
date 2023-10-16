#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <limits.h>

using namespace std;

int n, answer = INT_MAX;
int arr[1001][3];

int main()
{
    cin >> n;
    for (int i = 1; i <= n; i++)
        cin >> arr[i][0] >> arr[i][1] >> arr[i][2];
    
    for (int start = 0; start < 3; start++)
    {
        int dp[1001][3];
        dp[1][0] = 1000 * 1000 + 1;
        dp[1][1] = 1000 * 1000 + 1;
        dp[1][2] = 1000 * 1000 + 1;
        dp[1][start] = arr[1][start];
        for (int i = 2; i <= n; i++)
        {
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0];
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1];
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2];
        }

        for (int end = 0; end < 3; end++)
            if (start != end)
                answer = min(answer, dp[n][end]);
    }

    cout << answer;
}