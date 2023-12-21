#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

int n, m, start, last;
vector<string> board;
vector<int> edge[2500];
//{다음노드, 가중치}
vector<int> findDelta(int d)
{
    if (d == 0)
        return {0, 1};
    else if (d == 1)
        return {0, -1};
    else if (d == 2)
        return {1, 0};
    else   
        return {-1, 0};
}

int findNumber(int x, int y)
{
    return x * m + y;
}

vector<int> findPoint(int point)
{
    int x = point / m;
    int y = point % m;

    return {x, y};
}

vector<int> findDis(int x, int y)
{
    int g = 0;
    int n_g = 0;

    if (board[x][y] == 'g')
        g = 1;
    else
    {
        for (int d = 0; d < 4; d++)
        {
            vector<int> delta = findDelta(d);
            int nx = x + delta[0];
            int ny = y + delta[1];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                continue;
            if (board[nx][ny] == 'g')
                n_g++;
        }
    }
    return {g, min(n_g, 1)};     
}

vector<vector<int> > dis(2500, vector<int>(2, 1e9));
//{쓰레기 지난 수, 쓰레기 옆을 지난 수}
void    djk()
{
    priority_queue<tuple<int, int, int> > que;
    //{g, n_g, cur}
    que.push({-dis[start][0], -dis[start][1], start});
    while (!que.empty())
    {
        auto [g, n_g, cur] = que.top();
        // cout << g << " " << n_g << " " << cur << "\n";
        g *= -1;
        n_g *= -1;
        que.pop();
        for (int i = 0; i < edge[cur].size(); i++)
        {
            int next = edge[cur][i];
            vector<int> nextPoint = findPoint(next);
            vector<int> nextDis = findDis(nextPoint[0], nextPoint[1]);
            if (next == last)
                nextDis = {0, 0};
            nextDis[0] += g;
            nextDis[1] += n_g;

            if (dis[next][0] > nextDis[0])
            {
                dis[next][0] = nextDis[0];
                dis[next][1] = nextDis[1];
                que.push({-dis[next][0], -dis[next][1], next});
            }
            else if (dis[next][0] == nextDis[0] && dis[next][1] > nextDis[1])
            {
                dis[next][1] = nextDis[1];
                que.push({-dis[next][0], -dis[next][1], next});
            }
        }
    }
}

int main()
{
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string temp;

        cin >> temp;
        board.push_back(temp);
    }

    for (int x = 0; x < n; x++)
    {
        for (int y = 0; y < m; y++)
        {
            if (board[x][y] == 'S')
                start = findNumber(x, y);
            else if (board[x][y] == 'F')
                last = findNumber(x, y);
            
            // int count = 0;
            
            for (int d = 0; d < 4; d++)
            {
                vector<int> delta = findDelta(d);
                int nx = x + delta[0];
                int ny = y + delta[1];

                if (nx < 0 || nx >= n || ny < 0 || ny >= m)
                    continue;
                // if (board[nx][ny] == 'g')
                //     count++;
                edge[findNumber(x, y)].push_back(findNumber(nx, ny));
            }           
            if (board[x][y] == 'S')
                dis[start] = {0, 0};
        }
    }
    djk();
    cout << dis[last][0] << " " << dis[last][1];
}