#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int arr[100][100] = {{0,}};

int n, m, k;
int part = 0;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

void    draw(int x1, int y1, int x2, int y2)
{
    for (int i = x1; i < x2; i++)
    {
        for (int j = y1; j < y2; j++)
        {
            arr[j][i] = 1;
        }
    }
}

void    dfs(int x, int y)
{
    part++;
    arr[x][y] = 1;
    for (int l = 0; l < 4; l++)
    {
        int nx = x + dx[l];
        int ny = y + dy[l];

        if (nx < 0 || ny < 0 || nx >= m || ny >= n)
            continue;
        if (arr[nx][ny] == 1)
            continue;
        arr[nx][ny] = 1;
        dfs(nx, ny);
    }
}

int main()
{
    int answer = 0;
    cin >> m >> n >> k;
    vector<int> vec;
    while (k > 0)
    {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        draw(x1, y1, x2, y2);
        k--;
    }
    for (int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (arr[i][j] == 0)
            {
                answer++;
                dfs(i, j);
                vec.push_back(part);
                part = 0;
            }
        }
    }
    sort(vec.begin(), vec.end());
    cout << answer << "\n";
    for (int o : vec)
        cout << o << " ";
}