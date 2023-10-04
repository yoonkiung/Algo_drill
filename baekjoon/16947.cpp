#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int n;
int startNode;
bool visited[3001] = {false,};
bool isFindCircle = false;
pair<vector<int>, bool> pa[3001];
//    childList, isCircle

void    dfs(int node, vector<int> way)
{
    // cout << "path : " << node << "\n";
    if (startNode == node && way.size() >= 2)
    {
        // cout << "find circle\n";
        for (int path : way)
            pa[path].second = true;
        pa[startNode].second = true;
        isFindCircle = true;
        return;
    }
    visited[node] = true;
    for (int child : pa[node].first)
    {
        if (!visited[child])
        {
            way.push_back(child);
            dfs(child, way);
            way.pop_back();
        }
        else
        {
            if (child == startNode && way.size() >= 2)
                dfs(child, way);
        }
    }
    if (isFindCircle) return;
}

void    findCircle()
{
    for (int i = 1; i <= n; i++)
    {
        vector<int> nodes;
        startNode = i;
        memset(visited, false, sizeof(visited));
        dfs(i, nodes);
        // cout << "\n";
        if (isFindCircle)
            return ;
    }
}

int findLength(int x)
{
    if (pa[x].second)
        return 0;
    queue<pair<int, int> > que;
    //      node, depth
    memset(visited, false, sizeof(visited));
    int depth = 0;
    que.push(make_pair(x, depth));
    visited[x] = true;
    
    while (!que.empty())
    {
        x = que.front().first;
        depth = que.front().second;
        que.pop();
        if (pa[x].second)
            return (depth);
        for (int child : pa[x].first)
        {
            if (!visited[child])
            {
                que.push(make_pair(child, depth + 1));
                visited[child] = true;
            }
        }
    }
    return -1;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int n1, n2;
        
        cin >> n1 >> n2;
        pa[n1].first.push_back(n2);
        pa[n1].second = false;
        pa[n2].first.push_back(n1);
        pa[n2].second = false;
    }
    findCircle();
    // for (int i = 1; i < n + 1; i++)
    // {
    //     cout << "i : " << i << " isCircle : " << pa[i].second << "\n";
    // }
    for (int i = 1; i <= n; i++)
    {
        cout << findLength(i) << " ";
    }
}