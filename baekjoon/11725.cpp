#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int> > vec(100001);
int arr[100001];
int n;
bool visited[100001] = {{false,}};

void    dfs(int node)
{
    visited[node] = true;
    for(auto o : vec[node])
    {
        if (visited[o] == false)
        {
            arr[o] = node;  
            dfs(o);
        }
    }
    visited[false] = false;
}

int main()
{
    cin >> n;
    for (int i = 0; i < n - 1; i++)
    {
        int n1, n2;
        cin >> n1 >> n2;
        vec[n1].push_back(n2);
        vec[n2].push_back(n1);
    }
    dfs(1);
    for (int i = 1; i < n; i++)
    {
        cout << arr[i + 1] << "\n";
    }
}