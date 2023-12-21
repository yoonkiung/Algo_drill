#include <iostream>
#include <vector>
#include <string>
#include <limits.h>
#include <queue>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <string.h>

using namespace std;

/*

n개의 지점 m개의 도로와 w개의 웜홀
한 지점에서 시간여행하고 다시 출발지로 돌아왔을때 시간이 되돌아가는 경우가 있는지

*/

int main()
{
    int t;

    cin >> t;
    for (int test = 0; test < t; test++)
    {
        int n, m, w;
        vector<vector<int> > edge;

        cin >> n >> m >> w;
        for (int i = 0; i < m; i++)
        {
            int s, e, t;

            cin >> s >> e >> t;
            edge.push_back({s, e, t});
            edge.push_back({e, s, t});
        }
        for (int i = 0; i < w; i++)
        {
            int s, e, t;

            cin >> s >> e >> t;
            edge.push_back({s, e, -t});
        }

        int dis[501];

        for (int i = 1; i <= n; i++)
            dis[i] = 1e9;
        dis[1] = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < edge.size(); j++)
            {
                int cur = edge[j][0];
                int next = edge[j][1];               
                int cost = edge[j][2];

                if (/*dis[cur] != 1e9 && */dis[next] > dis[cur] + cost)
                    dis[next] = dis[cur] + cost;
            }
        }
        bool flag = false;
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < edge.size(); j++)
            {
                int cur = edge[j][0];
                int next = edge[j][1];               
                int cost = edge[j][2];

                if (dis[cur] != 1e9 && dis[next] > dis[cur] + cost)
                {
                    cout << "YES\n";
                    flag = true;
                    break;
                }
            }
            if (flag)
                break;
        }
        if (!flag)
            cout << "NO\n";
    }
}