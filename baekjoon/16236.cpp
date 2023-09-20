#include <iostream>
#include <queue>
#include <vector>
#include <tuple>
#include <algorithm>
#include <string.h>

using namespace std;

int n;
int arr[20][20];
int baby[2];
int babyBody = 2;
int curEatCount = 0;
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};


int bfs()
{
    int visited[20][20] = {{0,}};
    vector<tuple<int, int, int> > vec;
    queue<tuple<int, int, int> > que;
        // <x, y, depth>
    que.push({0, baby[0], baby[1]});
    visited[baby[0]][baby[1]] = 1;
    while (!que.empty())
    {
        int depth = get<0>(que.front());
        int x = get<1>(que.front());
        int y = get<2>(que.front());

        que.pop();
        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k], ny = y + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny] == 1 || arr[nx][ny] > babyBody)
                continue;
            if (arr[nx][ny] && arr[nx][ny] < babyBody)
                vec.push_back({depth + 1, nx, ny});
            que.push({depth + 1, nx, ny});
            visited[nx][ny] = 1;
        }
    }
    if (vec.size() == 0)
        return -1;
     
    sort(vec.begin(), vec.end());
    int x = get<1>(vec[0]);
    int y = get<2>(vec[0]);
    arr[baby[0]][baby[1]] = 0;
    baby[0] = x;
    baby[1] = y;
    curEatCount++;
    if (curEatCount == babyBody)
    {
        curEatCount = 0;
        babyBody++;
    }
    arr[x][y] = 9;
    return get<0>(vec[0]);
}

int main()
{    
    int time = 0;    
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 9)
            {
                baby[0] = i;
                baby[1] = j;   
            }
        }
    }
    while (true)
    {
        int temp = bfs();
        if (temp == -1)
        {
            cout << time;
            return (0);
        }
        time += temp;
    }
}