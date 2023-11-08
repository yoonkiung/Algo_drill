#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int n, k;
vector<pair<int, int> > vec;

void    findValue()
{
    vector<vector<int> > dp(n + 1, vector<int>(k + 1, 0));

    for (int i = 1; i < n + 1; i++)
    {
        for (int j = 1; j < k + 1; j++)
        {
            int w = vec[i - 1].first;
            int v = vec[i - 1].second;

            if (w > j)
                dp[i][j] = dp[i - 1][j];
            else
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v);
        }
    }
    cout << dp[n][k];
}


int main()
{
    cin >> n >> k;
    for (int i = 0; i < n; i++)
    {
        int w, v;
        cin >> w >> v;
        vec.push_back(make_pair(w, v));   
    }
    findValue();
}