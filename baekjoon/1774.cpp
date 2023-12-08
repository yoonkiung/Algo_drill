#include <iostream>
#include <vector>
#include <string>
#include <limits.h>
#include <queue>
#include <stdio.h>
#include <math.h>
#include <algorithm>

using namespace std;

/*
새로운 우주신들은 황선자씨와 연결된 우주신이랑 교감 가능
*/

pair<int, vector<int> > info[1001];

int find(int a)
{
    if (info[a].first == a)
        return a;
    return info[a].first = find(info[a].first);
}

void    uni(int a, int b)
{
    a = find(a);
    b = find(b);
    info[a].first = b;
}

double dis(int x1, int y1, int x2, int y2)
{
    return sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2));
}

bool isConnected(int a, int b)
{
    if (find(a) == find(b))
        return true;
    return false;
}

int cmp(pair<pair<int, int>, double> a, pair<pair<int, int>, double> b)
{
    return a.second < b.second;
}

int main()
{
    int n, m;
    double answer = 0;
    vector<pair<pair<int, int>, double> > edge;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int x, y;

        cin >> x >> y;
        info[i + 1].first = i + 1;
        info[i + 1].second = {x, y};
        for (int j = 0; j < i; j++)
        {
            int nx = info[j + 1].second[0];
            int ny = info[j + 1].second[1];

            edge.push_back({{i + 1, j + 1}, dis(x, y, nx, ny)});
        }
    }

    for (int i = 0; i < m; i++)
    {
        int a, b;
        
        cin >> a >> b;
        uni(a, b);
    }

    sort(edge.begin(), edge.end(), cmp);
    for (int i = 0; i < edge.size(); i++)
    {
        int a = edge[i].first.first;
        int b = edge[i].first.second;
        double cost = edge[i].second;

        if (isConnected(a, b))
            continue;
        answer += cost;
        uni(a, b);
    }
    printf("%.2lf", round(answer * 100) / 100);
}