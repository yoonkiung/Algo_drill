#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>
#include <string>

using namespace std;

vector<string> vec;

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int n, m;

int bfs(int start_x, int start_y)
{
    int answer = 0;
    bool visited[50][50] = {{0,}};
    queue<pair<pair<int, int>, int> > que;
    //         <좌표<x, y>, 거리>
    que.push(make_pair(make_pair(start_x, start_y), 0));
    while (!que.empty())
    {
        int x = que.front().first.first, y = que.front().first.second;
        int dis = que.front().second;
        que.pop();
        if (answer < dis)
            answer = dis;

        visited[x][y] = true;
        for (int i = 0; i < 4; i++)
        {
            int nx = x + dx[i], ny = y + dy[i];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] == true || vec[nx][ny] == 'W')
                continue;
            que.push(make_pair(make_pair(nx, ny), dis + 1));
            visited[nx][ny] = true;
        }
    }
    return (answer);
}

int main()
{
    int answer = 0;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        vec.push_back(temp);
    }
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (vec[i][j] == 'L')
            {
                int dis = bfs(i, j);
                if (dis > answer)
                    answer = dis;
            }               
        }
    }
    cout << answer;
}