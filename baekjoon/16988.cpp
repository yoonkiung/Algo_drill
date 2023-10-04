#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int n, m, maxAnswer = 0;
int arr[21][21];
vector<pair<int, int> > zero;
bool visited[21][21] = {{false,}};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int bfs(int x, int y)
{
    int answer = 0;
    queue<pair<int, int> > que;

    que.push(make_pair(x, y));
    visited[x][y] = true;
    while (!que.empty())
    {
        x = que.front().first;
        y = que.front().second;
        que.pop();
        answer++;
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || arr[nx][ny] == 1)
                continue;
            if (arr[nx][ny] == 0)
                answer = -100000000;
            if (arr[nx][ny] == 2)
            {
                visited[nx][ny] = true;
                que.push(make_pair(nx, ny));
            }
        }
    }
    return answer;
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 0)
                zero.push_back(make_pair(i, j));
        }
    }

    for (int i = 0; i < zero.size() - 1; i++)
    {
        for (int j = i + 1; j < zero.size(); j++)
        {
            int x1 = zero[i].first;
            int y1 = zero[i].second;
            int x2 = zero[j].first;
            int y2 = zero[j].second;

            arr[x1][y1] = 1;
            arr[x2][y2] = 1;
            int deletedEnemy = 0;
            memset(visited, false, sizeof(visited));
            for (int x = 0; x < n; x++)
            {
                for (int y = 0; y < m; y++)
                {
                    if (arr[x][y] == 2 && !visited[x][y])
                    {
                        int temp = bfs(x, y);
                        if (temp > 0)
                            deletedEnemy += temp;
                        // cout << x << " " << y << " " << deletedEnemy << "\n";
                    }
                }
            }
            maxAnswer = max(maxAnswer, deletedEnemy);
            arr[x1][y1] = 0;
            arr[x2][y2] = 0;
        }
    }
    cout << maxAnswer;
}