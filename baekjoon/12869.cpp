#include <iostream>
#include <vector>
#include <string>
#include <string.h>
#include <queue>
#include <limits.h>

using namespace std;

int answer = INT_MAX;
int visited[61][61][61] = {{{0,}}};

void    dfs(int h1, int h2, int h3, int depth)
{
    if (h1 == 0 && h2 == 0 && h3 == 0)
    {
        answer = min(depth, answer);
        return ;
    }
    if (visited[h1][h2][h3] <= depth && visited[h1][h2][h3] != 0)
        return ;
    visited[h1][h2][h3] = depth;
    dfs(max(h1 - 9, 0), max(h2 - 1, 0), max(h3 - 3, 0), depth + 1);
    dfs(max(h1 - 9, 0), max(h2 - 3, 0), max(h3 - 1, 0), depth + 1);
    dfs(max(h1 - 3, 0), max(h2 - 9, 0), max(h3 - 1, 0), depth + 1);
    dfs(max(h1 - 3, 0), max(h2 - 1, 0), max(h3 - 9, 0), depth + 1);
    dfs(max(h1 - 1, 0), max(h2 - 9, 0), max(h3 - 3, 0), depth + 1);
    dfs(max(h1 - 1, 0), max(h2 - 3, 0), max(h3 - 9, 0), depth + 1);
}

int scv[3] = {0,};

int main()
{
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> scv[i];
    dfs(scv[0], scv[1], scv[2], 0);
    cout << answer;
}
