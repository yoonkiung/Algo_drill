#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int room = 0;
int roomMax = -1;
int roomMaxRemoveWall = -1;
int n, m;
int arr[50][50];
int dx[4] = {0, -1, 0, 1};
int dy[4] = {-1, 0, 1, 0};

int calRoom(int x, int y, bool visited[50][50])
{
    int depth = 1;
    queue<pair<int, int> > que;

    que.push(make_pair(x, y));
    visited[x][y] = true;
    while (!que.empty())
    {
        x = que.front().first;
        y = que.front().second;
        que.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] == true)
                continue;
            else if (k == 0 && (arr[x][y] & 1)) // 서
                continue;
            else if (k == 1 && (arr[x][y] & 2)) // 북
                continue;
            else if (k == 2 && (arr[x][y] & 4)) //동
                continue;
            else if (k == 3 && (arr[x][y] & 8)) //남
                continue;
            que.push(make_pair(nx, ny));
            visited[nx][ny] = true;
            depth++;
        }  
    }
    return (depth);
}

int breakWall(int x, int y)
{
    int maxValue = -1;
    for (int k = 0; k < 4; k++)
    {
        if (k == 0 && (arr[x][y] & 1)) // 서
        {
            bool visited[50][50] = {{false,}};
            arr[x][y] -= 1;
            int temp = calRoom(x, y, visited);
            if (temp > maxValue)
                maxValue = temp;
            arr[x][y] += 1;
        }
        else if (k == 1 && (arr[x][y] & 2)) // 북
        {
            bool visited[50][50] = {{false,}};
            arr[x][y] -= 2;
            int temp = calRoom(x, y, visited);
            if (temp > maxValue)
                maxValue = temp;
            arr[x][y] += 2;
        }
        else if (k == 2 && (arr[x][y] & 4)) //동
        {
            bool visited[50][50] = {{false,}};
            arr[x][y] -= 4;
            int temp = calRoom(x, y, visited);
            if (temp > maxValue)
                maxValue = temp;
            arr[x][y] += 4;
        }
        else if (k == 3 && (arr[x][y] & 8)) //남
        {
            bool visited[50][50] = {{false,}};
            arr[x][y] -= 8;
            int temp = calRoom(x, y, visited);
            if (temp > maxValue)
                maxValue = temp;
            arr[x][y] += 8;
        }
    }
    return (maxValue);
}

int main()
{
    bool visited[50][50] = {{false}};

    cin >> m >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cin >> arr[i][j];
    }

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (!visited[i][j])
            {
                room++;
                //벽 허물기전 BFS
                int temp = calRoom(i, j, visited);
                if (temp > roomMax)
                    roomMax = temp;
                if (temp > roomMaxRemoveWall)
                    roomMaxRemoveWall = temp;
                //벽 허물고 BFS
                temp = breakWall(i, j);
                if (temp > roomMaxRemoveWall)
                    roomMaxRemoveWall = temp;
            }
            else
            {
                //벽 허물고 BFS
                int temp = breakWall(i, j);
                if (temp > roomMaxRemoveWall)
                    roomMaxRemoveWall = temp;
            }
        }
    }
    cout << room << "\n" << roomMax << "\n" << roomMaxRemoveWall;
}
