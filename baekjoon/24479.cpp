#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, m, r;
vector<int> vec[100001];
int arr[100001] = {0,};
bool visited[100001] = {false,};
int depth = 1;

void    dfs(int node)
{
    arr[node] = depth++;
    visited[node] = true;
    sort(vec[node].begin(), vec[node].end());
    for (auto o : vec[node])
    {
        if (visited[o] == false)
        {
            visited[o] = true;
            dfs(o);
        }
    }
}

int main()
{
    cin >> n >> m >> r;
    for (int i = 0; i < m; i++)
    {
        int u, v;
        cin >> u >> v;
        vec[u].push_back(v);
        vec[v].push_back(u);
    }
    dfs(r);
    for (int i = 1; i < n + 1; i++)
        cout << arr[i] << "\n";
    return (0);
}