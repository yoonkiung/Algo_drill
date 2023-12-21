#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

vector<vector<int> > edge;

int cmp(vector<int> a, vector<int> b)
{
    return a[2] < b[2];
}

int vertex[10001];

int find(int a)
{
    if (vertex[a] == a)
        return a;
    return vertex[a] = find(vertex[a]);
}

void uni(int a, int b)
{
    a = find(a);
    b = find(b);

    vertex[a] = b;
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);

    int v, e, answer = 0, node = 0;
    cin >> v >> e;
    for (int i = 1; i <= 10000; i++)
        vertex[i] = i;
    for (int i = 0; i < e; i++)
    {
        int a, b, c;

        cin >> a >> b >> c;
        edge.push_back({a, b, c});
    }
    sort(edge.begin(), edge.end(), cmp);
    
    for (vector<int> info : edge)
    {
        int a = find(info[0]);
        int b = find(info[1]);
        int cost = info[2];

        if (a == b)
            continue;
        uni(a, b);
        answer += cost;
        node++;
        if (node == v - 1)
            break;
    }
    cout << answer;
}