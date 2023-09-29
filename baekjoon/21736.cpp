#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>

using namespace std;

int     n, m, answer;
char    arr[601][601];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
bool visited[601][601] = {{false, }};

void    dfs(int x, int y)
{
    visited[x][y] = true;

    for (int k = 0; k < 4; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx < 0 || nx >= n | ny < 0 || ny >= m || visited[nx][ny] || arr[nx][ny] == 'X')
            continue;
        if (arr[nx][ny] == 'P')
            answer++;
        visited[nx][ny] = true;
        dfs(nx, ny);
    }
}


int main()
{
    cin >> n >> m;
    int x, y;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 'I')
            {
                x = i;
                y = j;
            }
        }           
    }
    dfs(x, y);
    if (!answer)
        cout << "TT";
    else
        cout << answer;
}