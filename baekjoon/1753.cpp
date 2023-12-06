#include <iostream>
#include <vector>
#include <string>
#include <limits.h>
#include <queue>

using namespace std;

vector<pair<int, int> > a[20001];
int d[20001];

void    djk(int start)
{
    priority_queue<pair<int, int> > que;

    que.push(make_pair(0, start));
    while (!que.empty())
    {
        int current = que.top().second;
        int distance = -que.top().first;
        
        que.pop();
        if (d[current] < distance)
            continue;
        for (int i = 0; i < a[current].size(); i++)
        {
            int next = a[current][i].first;
            int nextDis = distance + a[current][i].second;

            if (nextDis < d[next])
            {
                d[next] = nextDis;
                que.push(make_pair(-nextDis, next));
            }
        }
    }
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);

    int n, e, start;
    
    cin >> n >> e >> start;
    for (int i = 0; i <= n; i++)
        d[i] = INT_MAX;
    for (int i = 0; i < e; i++)
    {
        int u, v, w;
        
        cin >> u >> v >> w;
        a[u].push_back(make_pair(v, w));
        
    }
    
    d[start] = 0;
    djk(start);

    for (int i = 1; i <= n; i++)
    {
        if (i == start)
            cout << 0 << "\n";
        else if (d[i] == INT_MAX)
            cout << "INF\n";
        else
            cout << d[i] << "\n";
    }
}