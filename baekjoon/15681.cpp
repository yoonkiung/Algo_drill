#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int n, r, q, u;
vector<int> vec[100001];

int arr[100001] = {0,};
bool visited[100001] = {false,};

int dfs(int node)
{
    visited[node] = true;
    for (int child : vec[node])
    {
        if (!visited[child])
        {
            visited[child] = true;
            arr[node] += dfs(child);
        }
    }
    arr[node]++;
    return arr[node];
}

int main()
{
    // std::cin.tie(0);
    // std::cout.tie(0);
    // std::ios_base::sync_with_stdio(false);
    // cin >> n >> r >> q;
    scanf("%d%d%d", &n, &r, &q);
    for (int i = 0; i < n - 1; i++)
    {
        int n1, n2;
        // cin >> n1 >> n2;
        scanf("%d%d", &n1, &n2);

        vec[n1].push_back(n2);
        vec[n2].push_back(n1);
    }
    dfs(r);
    for (int i = 0; i < q; i++)
    {
        // cin >> u;
        // cout << arr[u] << "\n";
        scanf("%d", &u);
        printf("%d\n", arr[u]);
    }
}