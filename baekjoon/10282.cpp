#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

int t, n, d, c;

int main()
{
    ios::sync_with_stdio(false); cin.tie(NULL);
    int t;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        vector<vector<int> > edge[10001]; //{다음노드, 가중치}
        priority_queue<pair<int, int> > que;  //{-가중치, 다음노드}
        int dis[10001];

        cin >> n >> d >> c;
        memset(edge, 1e9, sizeof(edge));
        memset(dis, 1e9, sizeof(dis));
        for (int i = 1; i <= n; i++)
            dis[i] = 1e9;
        for (int j = 0; j < d; j++)
        {
            int a, b, s;
            
            cin >> a >> b >> s;
            edge[b].push_back({a, s});
        }
        dis[c] = 0;
        que.push({0, c});
        while (!que.empty())
        {
            int cur = que.top().second;
            int curDis = -que.top().first;

            que.pop();
            for (int k = 0; k < edge[cur].size(); k++)
            {
                int next = edge[cur][k][0];
                int nextDis = edge[cur][k][1] + curDis;
                // cout << next << " " << nextDis << " " << dis[next] << "\n";
                if (nextDis < dis[next])
                {
                    dis[next] = nextDis;
                    que.push({-nextDis, next});
                }
            }
        }
        int count = 0, time = 0;
        for (int k = 1; k <= n; k++)
        {
            if (k == c)
                continue;
            if (dis[k] != 1e9)
            {
                count++;
                time = max(time, dis[k]);
            }
        }
        cout << count + 1 << " " << time << "\n";
    }
}