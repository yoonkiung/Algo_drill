#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec[101];
bool visited[101] = {false,};
int n, k, answer = -1;
int arr[2];


void    dfs(int node, int depth)
{
    // cout << "node : " << node << "\n";
    if (arr[1] == node)
    {
        answer = depth;
        return;
    }
    visited[node] = true;
    for(auto o : vec[node])
    {
        if (visited[o] == false)
            dfs(o, depth + 1);  
    }
    // visited[node] = false;
}

int main()
{
    cin >> n >> arr[0] >> arr[1] >> k;

    for (int i = 0; i < k; i++)
    {
        int n1, n2;
        cin >> n1 >> n2;
        vec[n1].push_back(n2);
        vec[n2].push_back(n1);
    }
    dfs(arr[0], 0);
    cout << answer;
}