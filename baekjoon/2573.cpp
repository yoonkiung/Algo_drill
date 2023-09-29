#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int n, m, ans = 0;
int arr[301][301];
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

bool melt()
{
    int temp[301][301];
    bool flag = false;
    memcpy(temp, arr, sizeof(int) * 300 * 300);
    for (int i = 1; i < n - 1; i++)
    {
        for (int j = 1; j < m - 1; j++)
        {
            if (temp[i][j] > 0)
            {
                flag = true;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
            
                    if (temp[nx][ny] == 0)
                        arr[i][j] = max(arr[i][j] - 1, 0);
                }
            }           
        }
    }
    // cout << flag << "melt return\n";
    return (flag);
}

bool isConnect()
{
    // cout << "in connect" << "\n";
    bool isAllZero = true;
    int land = 0;
    bool visited[300][300] = {{false,}};
    queue<pair<int, int> > que;

    for (int i = 1; i < n - 1; i++)
    {
        for (int j = 1; j < m - 1; j++)
        {
            if (arr[i][j] > 0 && !visited[i][j])
            {
                isAllZero = false;
                if (land >= 1)
                    return false;
                else
                    land++;
                que.push(make_pair(i, j));
                visited[i][j] = true;
                while (!que.empty())
                {
                    int x = que.front().first;
                    int y = que.front().second;
                    que.pop();

                    for (int k = 0; k < 4; k++)
                    {
                        int nx = x + dx[k];
                        int ny = y + dy[k];

                        if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] == true || arr[nx][ny] == 0)
                            continue;
                        visited[nx][ny] = true;
                        que.push(make_pair(nx, ny));
                    }
                }
            }
        }
    }
    if (isAllZero)
    {
        cout << 0;
        exit(0);
    }
    return (land == 1);
}


int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cin >> arr[i][j];
    }

    int day = 0;
    while (true)
    {
        if (!melt())
        {
            cout << 0;
            return 0;
        }
        else if (!isConnect())
        {
            cout << day + 1;
            return 0;
        }
        day++;
    }
}