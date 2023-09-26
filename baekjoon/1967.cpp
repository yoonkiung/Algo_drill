#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n, answer = 0;
vector<pair<int, int> > vec[10001];
//          child, weight

void    dfs(int node, int weight, bool *visited)
{
    

    for (auto o : vec[node])
    {
        if (visited[o.first] == false)
        {
            int child = o.first;
            int newWeight = o.second + weight;

            answer = max(answer, newWeight);
            visited[node] = true;
            dfs(child, newWeight, visited);
        }
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int parent, child, weight;
        cin >> parent >> child >> weight;
        vec[parent].push_back(make_pair(child, weight));
        vec[child].push_back(make_pair(parent, weight));
    }   
    for (int i = 1; i <= n; i++)
    {
        bool visited[10001] = {false,};
        dfs(i, 0, visited);
    }       
    cout << answer;
}