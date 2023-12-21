#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>
#include <queue>

using namespace std;

/*
다리의 길이는 격자에서 차지하는 칸의 수

모든 섬 연결이 목표

다리의 방향이 중간이 바뀌면 안됨 
다리의 길이는 2 이상
A와 B를 연결하는 다리가 C와 인접한다해서 C랑 연결된게 아님

바다에서 다리는 중복 가능

모든 섬을 연결하는 다리의 최소값 구하기
*/

int board[10][10];
bool visited[10][10];
int n, m;
int info[10];

vector<vector<int> > edge;
// {a, b, 가중치}
vector<int> findDelta(int d)
{
    if (d == 0)
        return {0, 1};
    else if (d == 1)
        return {1, 0};
    else if (d == 2)
        return {-1, 0};
    else
        return {0, -1};
}

void    dfs(int x, int y, int& land_num)
{
    board[x][y] = land_num;

    for (int d = 0; d < 4; d++)
    {
        vector<int> delta = findDelta(d);
        int nx = x + delta[0];
        int ny = y + delta[1];
        if (nx < 0 || nx >= n || ny < 0 || ny >= m || visited[nx][ny] || board[nx][ny] != 1)
            continue;
        visited[nx][ny] = true;
        dfs(nx, ny, land_num);
    }
}

int find(int a)
{
    if (a == info[a])
        return a;
    return info[a] = find(info[a]);
}

void    uni(int a, int b)
{
    a = find(a);
    b = find(b);
    if (a == b)
        return;
    info[a] = b;
}

int land_num = 1;

void    sepLand()
{
    
    memset(visited, false, sizeof(visited));
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (!visited[i][j] && board[i][j] == 1)
            {
                info[land_num] = land_num;               
                visited[i][j] = true;
                dfs(i, j, land_num);
                land_num++;
            }
        }
    }
}

void    makeEdge()
{   
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] >= 1)
            {
                for (int d = 0; d < 4; d++)
                {
                    int x = i;
                    int y = j;
                    vector<int> delta = findDelta(d);
                    
                    while (x >= 0 && x < n && y >= 0 && y < m)
                    {
                        x += delta[0];
                        y += delta[1];
                        if (x < 0 || x >= n || y < 0 || y >= m)
                            break;
                        if (board[x][y] == board[i][j])
                            break;
                        if (board[x][y] == 0)
                        {
                            continue;
                        }
                        else if (board[x][y] != 0 && board[x][y] != board[i][j])
                        {
                            // cout << x << " " << y << " " << i << " " << j << "\n";
                            if (abs(x - i) + abs(y - j) - 1 >= 2)
                                edge.push_back({board[i][j], board[x][y], abs(x - i) + abs(y - j) - 1});
                            break;
                        }       
                    }
                }
            }
        }
    }  
}

int cmp(vector<int> a, vector<int> b)
{
    return a[2] < b[2];
}

int main()
{
    int answer = 0;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
            cin >> board[i][j];
    }
    sepLand();
    // for (int i = 0; i < n; i++)
    // {
    //     for (int j = 0; j < m; j++)
    //     {
    //         cout << board[i][j] << " ";
    //     }
    //     cout << "\n";
    // }
    makeEdge();
    
    sort(edge.begin(), edge.end(), cmp);
    for (vector<int> e : edge)
    {
        int a = e[0];
        int b = e[1];
        int cost = e[2];

        if (find(a) == find(b))
            continue;
        uni(a, b);
        answer += cost;
    }
    int dep =find(1);
    for (int i = 2; i < land_num; i++)
    {
        if (dep != find(i))
        {
            cout << -1;
            return 0;
        }
    }
    cout << answer;
}