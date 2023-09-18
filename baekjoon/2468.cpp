#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int arr[100][100] = {{0,}};
int n;

int bfs(int height)
{
    bool visited[100][100] = {{false,}};
    int answer = 0;
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (arr[i][j] >= height && !visited[i][j])
            {
                answer++;
                queue<pair<int, int> > que;

                que.push(make_pair(i, j));
                while (!que.empty())
                {
                    int x = que.front().first, y = que.front().second;
                    // visited[x][y] = true;
                    que.pop();
                    for (int k = 0; k < 4; k++)
                    {
                        int nx = x + dx[k];
                        int ny = y + dy[k];

                        if (nx < 0 || nx >= n || ny < 0 || ny >= n)
                            continue;
                        if (!visited[nx][ny] && arr[nx][ny] >= height)
                        {
                            que.push(make_pair(nx, ny));
                            visited[nx][ny] = true;
                        }
                    }
                }
            }
        }
    }
    return (answer);
}

int main()
{
    int max = -1;
    int big = -1;
    int less = 101;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int temp;
            cin >> temp;
            if (temp > big)
                big = temp;
            if (temp < less)
                less = temp;
            arr[i][j] = temp;
        }
    }
    for (int i = less; i <= big; i++)
    {
        int answer = bfs(i);
        if (answer > max)
            max = answer;
    }
    cout << max;
}