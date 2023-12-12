#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>
#include <queue>

using namespace std;

/*
오민식은 최대 이윤을 남기려고 한다.

n개의 도시 0 ~ n - 1까지의 번호

A도시에서 B도시로 여행
교통 수단은 다양함 --> 출발, 도착, 비용 알고있음
도시 방문때마다 돈 벌 수 있음

도착 도시에 도착할 때 가지고 있는 돈의 액수를 최대로 하려고 한다
이 최대값을 구하시오

버는 돈보다 쓰는 돈이 많다면 돈의 액수가 음수가 될 수도 있음
같은 도시 여러번 방문 가능, 방문할때마다 돈 번다
교통수단도 여러번 이용 가능

*/

long long  n, start, last, m;
vector<vector<long long > > edge;
long long  money[50];
vector<int> node[50];
//{시작, 끝, cost}

bool isConnected(int a, int b)
{
    queue<int> que;
    bool visited[50];

    memset(visited, false, sizeof(visited));
    que.push(a);
    while (!que.empty())
    {
        int cur = que.front();

        que.pop();
        for (int child : node[cur])
        {
            if (b == child)
                return true;
            if (visited[child])
                continue;
            if (child == b)
                return true;
            que.push(child);
            
        }
        visited[cur] = true;
    }
    return false;
}

bool belman()
{
    for (long long i = 0; i < n; i++)
    {
        for (long long j = 0; j < edge.size(); j++)
        {
            long long a = edge[j][0];
            long long b = edge[j][1];
            long long cost = edge[j][2];

            if (money[a] != 1e9 && money[b] > money[a] + cost)
            {
                money[b] = money[a] + cost;
            }
        }
    }
    for (long long i = 0; i < n; i++)
    {
        for (long long j = 0; j < edge.size(); j++)
        {
            long long a = edge[j][0];
            long long b = edge[j][1];
            long long cost = edge[j][2];

            if (money[a] != 1e9 && money[b] > money[a] + cost)
            {
                // cout << a << " " << b << " " << cost << "\n";
                if (isConnected(b, last))
                    return false;
                // if (b == last)
                //     return false;
            }
        }
    }
    return true;
}

int  main()
{
    cin >> n >> start >> last >> m;
    for (long long  i = 0; i < m; i++)
    {
        long long  a, b, cost;

        cin >> a >> b >> cost;
        edge.push_back({a, b, cost});
        node[a].push_back(b);
    }
    for (long long  i = 0; i < n; i++)
    {
        long long  earn;

        cin >> earn;
        money[i] = 1e9;
        if (i == start)
            money[i] = -earn;
        for (long long  j = 0; j < edge.size(); j++)
        {
            if (edge[j][1] == i)
                edge[j][2] -= earn;
        }
    }
    // for (auto e : edge)
    //     cout << e[0] << " " << e[1] << " " << e[2] << "\n";
    if (!belman())
    {
        if (money[last] == 1e9)
            cout << "gg";
        else
            cout << "Gee";
    }
    else
    {
        if (money[last] == 1e9)
            cout << "gg";
        else
            cout << -money[last];
    }
}