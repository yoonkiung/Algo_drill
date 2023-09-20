#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <string.h>

using namespace std;

int arr[100][100], temp[100][100];
int exCount = 0;
int n, m;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int isOpen(int i, int j)
{
    queue<pair<int, int> > que;
    int visited[100][100] = {{0,}};

    que.push(make_pair(i, j));
    visited[i][j] = 1;
    while (!que.empty())
    {
        int x = que.front().first, y = que.front().second;
        que.pop();
        visited[x][y] = 1;
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k], ny = y + dy[k];
            
            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                return (1);
            else if (visited[nx][ny] == 1)
                continue;
            else if (temp[nx][ny] == 0)
            {
                que.push(make_pair(nx, ny));
                visited[nx][ny] = 1;
            }
        }
    }
    return (0);
}

int bfs()
{
    int flag = 0;    
    int visited[100][100] = {{0,}};
    int tempExcount = exCount;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (temp[i][j] == 0 && !visited[i][j] && isOpen(i, j))
            {
                // cout << i << " " << j << "\n";
                queue<pair<int, int> > que;
                que.push(make_pair(i, j));
                visited[i][j] = 1;
                while (!que.empty())
                {
                    int x = que.front().first, y = que.front().second;
                    que.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx = x + dx[k];
                        int ny = y + dy[k];
                        
                        if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                            continue;
                        else if (temp[nx][ny] == 1 &&  arr[nx][ny] == 1)
                        {
                            arr[nx][ny] = 0;
                            tempExcount--;
                        }
                        else if (visited[nx][ny] == 0 && temp[nx][ny] == 0)
                        {
                            que.push(make_pair(nx, ny));
                            visited[nx][ny] = 1;
                        }
                    }
                }
            }
            else if (temp[i][j] == 1)
                flag = 1;
        }
    }
    if (flag == 1)
    {
        exCount = tempExcount;
    }
        
    return flag;
}


int main()
{
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 1)
                exCount++;
        }
    }
    
    int depth = 0;
    vector<int> count;
    while (true)
    {
        count.push_back(exCount);
        memcpy(temp, arr, sizeof(int) * 100 * 100);
        int flag = bfs();
        if (!flag)
        {
            cout << depth << "\n";
            cout << count[depth - 1];
            break;
        }
        depth++;
    }
}