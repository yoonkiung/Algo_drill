#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int n, l, r, answer = 0;
int arr[50][50];

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

int bfs(int i, int j, int temp[50][50], bool visited[50][50])
{
    int people = arr[i][j];
    vector<pair<int, int> > pos;
    queue<pair<int, int> > que;

    que.push(make_pair(i, j));
    pos.push_back(make_pair(i, j));
    visited[i][j] = true;
    while (!que.empty())
    {
        int x = que.front().first, y = que.front().second;
        que.pop();

        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k], ny = y + dy[k];
            if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny])
                continue;
            int diff = abs(arr[nx][ny] - arr[x][y]); 
            if (diff >= l &&  diff <= r)
            {
                people += arr[nx][ny];
                pos.push_back(make_pair(nx, ny));
                que.push(make_pair(nx, ny));
                visited[nx][ny] = true;
            }
        }
    }
    if (pos.size() >= 2)
    {
        int ave = people / pos.size();
        for (auto o : pos)
            temp[o.first][o.second] = ave;
        return (1);
    }
    else
        return (0);
}

int day()
{
    bool visited[50][50] = {{false,}};
    int temp[50][50];
    int isChange = 0;

    memcpy(temp, arr, sizeof(int) * 50 * 50);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                int flag = bfs(i, j, temp, visited);
                if (flag)
                    isChange = 1;
            }
        }
    }
    memcpy(arr, temp, sizeof(int) * 50 * 50);
    return (isChange);
}

int main()
{
    cin >> n >> l >> r;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cin >> arr[i][j];
    }
    while (true)
    {
        if (!day())
            break;
        answer++;
    }
    cout << answer;
}
