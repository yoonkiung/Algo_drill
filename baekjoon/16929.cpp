#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>

using namespace std;

int n, m;
char arr[51][51];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int originX, originY;
bool visited[51][51];

void    dfs(int x, int y, int depth)
{
    if (x == originX && y == originY && depth >= 4)
    {
        // cout << x << originX << y << originY;
        cout << "Yes";
        exit(0);
    }

    for (int k = 0; k < 4; k++)
    {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || arr[nx][ny] != arr[x][y])
            continue;
        visited[nx][ny] = true;
        dfs(nx, ny, depth + 1);
        visited[nx][ny] = false;
    }
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            memset(visited, false, sizeof(visited));
            originX = i;
            originY = j;
            dfs(i, j, 1);
        }
    }   
    cout << "No";
}