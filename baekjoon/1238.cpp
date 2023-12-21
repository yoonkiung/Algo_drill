#include <iostream>
#include <vector>
#include <string>
#include <limits.h>
#include <queue>

using namespace std;

int n, m, x;
vector<pair<int, int> > a[1001];
int d[1001][1001];

void    djk(int start)
{
    d[start][start] = 0;

    priority_queue<pair<int, int> > que;
    que.push(make_pair(0, start));

    while (!que.empty())
    {
        int current = que.top().second;
        int distance = -que.top().first;
        que.pop();
        if (d[start][current] < distance)
            continue;
        for (int i = 0; i < a[current].size(); i++)
        {
            int next = a[current][i].first;
            int nextDis = a[current][i].second + distance;

            if (nextDis < d[start][next])
            {
                d[start][next] = nextDis;
                que.push(make_pair(-nextDis, next));
            }
        }
    }
}

int maxValue = -1;

int main()
{

    cin >> n >> m >> x;
    for (int i = 0; i < 1001; i++)
        for (int j = 0; j < 1001; j++)
            d[i][j] = INT_MAX;
    
    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        a[u].push_back(make_pair(v, w));
    }
    for (int i = 1; i < n + 1; i++)
        djk(i);
    for (int i = 1; i < n + 1; i++)
        maxValue = max(maxValue, d[i][x] + d[x][i]);   
    cout << maxValue;
}