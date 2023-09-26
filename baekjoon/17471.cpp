#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, answer = 1000000000;
int arr[11];
vector<int> vec[11];
bool selected[11] = {false,};
bool isDivide = false;

bool    isConnected(vector<int>& v, bool flag)  
{
    queue<int> que;
    bool visited[11] = {false,};

    que.push(v[0]);
    visited[v[0]] = true;
    int queSize = 0;
    while (!que.empty())
    {
        int nx = que.front();

        que.pop();
        queSize++;
        for (int child : vec[nx])
        {
            if (!visited[child] && selected[child] == flag)
            {
                que.push(child);
                visited[child] = true;
            }
        }
    }
    return (queSize == v.size());
}

void    dfs(int idx, int depth)
{
    if (depth >= 1)
    {
        vector<int> a, b;
        int sumA = 0, sumB = 0;

        for (int i = 1; i <= n; i++)
        {
            if (selected[i])
            {
                a.push_back(i);
                sumA += arr[i];
            }
            else
            {
                b.push_back(i);
                sumB += arr[i];
            }
        }
        if (a.size() != 0 && b.size() != 0 && isConnected(a, true) && isConnected(b, false))
        {
            isDivide = true;
            answer = min(answer, abs(sumA - sumB));
        }
    }

    for (int i = idx; i <= n; i++)
    {
        if (selected[i])
            continue;
        selected[i] = true;
        dfs(i + 1, depth + 1);
        selected[i] = false;
    }
}


int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i + 1];
    for (int i = 0; i < n; i++)
    {
        int num;
        cin >> num;
        for (int j = 0; j < num; j++)
        {
            int child;
            cin >> child;
            vec[i + 1].push_back(child);
            vec[child].push_back(i + 1);
        }
    }
    dfs(1, 0);
    if (isDivide)
        cout << answer;
    else
        cout << -1;
}