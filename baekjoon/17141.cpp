#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string>
#include <string.h>

using namespace std;

int arr[50][50] = {{0,}};
int answer = -1;
int curArr[50][50];
int n, m;
bool selected[10] = {false,};

int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};

vector<pair<int, int> > vec;
vector<pair<int, int> > combi;

int bfs()
{
    int maxValue = 0;
    bool visited[50][50] = {{false,}};
    memcpy(curArr, arr, sizeof(int) * 50 * 50);
    queue<pair<pair<int, int>, int> > que;
    //    <x, y>, depth
    for (auto a : combi)
    {
        curArr[a.first][a.second] = -1;
        que.push(make_pair(a, 0));
        visited[a.first][a.second] = true;
    }

    while (!que.empty())
    {
        int x = que.front().first.first, y = que.front().first.second;
        int depth = que.front().second;
        que.pop();

        for (int k = 0; k < 4; k++)
        {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= n || visited[nx][ny])
                continue;
            if (curArr[nx][ny] == 1 || curArr[nx][ny] == -1)
                continue;
            // maxValue = maxValue ? depth + 1 : maxValue > depth + 1;
            maxValue = max(maxValue, depth + 1);
            curArr[nx][ny] = depth + 1;
            que.push(make_pair(make_pair(nx, ny), depth + 1));
            visited[nx][ny] = true;
        }
    }
    int flag = false;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (curArr[i][j] != -1)
                flag = true;
            if (curArr[i][j] == 0)
                return  (-1);
        }
    }
    if (!flag)
        return 0;
    return maxValue;
}

void makeCombi(int idx, int cnt)
{
    if (cnt == m)
    {
        int virus = bfs();
        
        if (virus != -1)
        {
            if (answer == -1)
                answer = virus;
            else
                if (answer > virus)
                    answer = virus;
        }
    }
    else
    {
        for (int i = idx; i < vec.size(); i++)
        {
            if (selected[i] == true) continue;
            selected[i] = true;
            combi.push_back(vec[i]);
            makeCombi(i, cnt + 1);
            combi.pop_back();
            selected[i] = false;
        }
    }
}

int main()
{
    
    cin >> n >> m;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> arr[i][j];
            if (arr[i][j] == 2)
            {
                arr[i][j] = 0;
                vec.push_back(make_pair(i, j));
            }
                
        }           
    }
    makeCombi(0, 0);
    cout << answer;
}