#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

int dis[101][101];

int main()
{
    int n, m;

    cin >> n >> m;
    for (int i = 0; i <= n; i++)
    {
        for (int j = 0; j <= n; j++)
        {
            dis[i][j] = 1e9;
            if (i == j)
                dis[i][j] = 0;
        }
    }
    for (int i = 0; i < m; i++)
    {
        int a, b, c;

        cin >> a >> b >> c;
        dis[a][b] = min(c, dis[a][b]);
    }
    for (int middle = 1; middle <= n; middle++)
    {
        for (int start = 1; start <= n; start++)
        {
            for (int end = 1; end <= n; end++)
                dis[start][end] = min(dis[start][end], dis[start][middle] + dis[middle][end]);
        }
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            if (dis[i][j] == 1e9)
                cout << 0 << " ";
            else
                cout << dis[i][j] << " ";
        }
        cout << "\n";
    }
}