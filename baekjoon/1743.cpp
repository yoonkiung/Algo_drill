#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int arr[100][100] = {{0,}}; //빈칸 : 0, 음식물 = 1
bool visited[100][100] = {{false,}};
int n, m, k;
int answer = -1;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int area = 1;

void dfs(int x, int y)
{
    visited[x][y] = true;

    for (int l = 0; l < 4; l++)
    {
        int nx = x + dx[l];
        int ny = y + dy[l];

        if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny])
            continue;
        if (arr[nx][ny] == 1)
        {
            visited[nx][ny] = true;
            area++;
            dfs(nx, ny);
        }
    }
}

int main()
{
    cin >> n >> m >> k;
    for (int i = 0; i < k; i++)
    {
        int x, y;
        
        cin >> x >> y;
        arr[x - 1][y - 1] = 1;
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (arr[i][j] && !visited[i][j])
            {
                dfs(i, j);
                if (answer < area)
                    answer = area;
                area = 1;
            }
        }
    }
    cout << answer;
}