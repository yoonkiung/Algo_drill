#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int r, c, t, answer = 0;
int arr[50][50];
int temp[50][50];


vector<pair<int, int> > air;

void    swapPos(int x1, int y1, int x2, int y2)
{
    int tmp = arr[x1][y1];
    arr[x1][y1] = arr[x2][y2];
    arr[x2][y2] = tmp;
}

void operateAirUp()
{
    bool visited[50][50];
    int x = air[0].first, y = air[0].second;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (i == x || j == y || i == 0 || j == c - 1)
                visited[i][j] = false;
            else
                visited[i][j] = true;
        }
    }
    while (true)
    {
        int dx[4] = {-1, 0, 1, 0};
        int dy[4] = {0, 1, 0, -1};
        int nx, ny;
        for (int k = 0; k < 4; k++)
        {
            nx = x + dx[k];
            ny = y + dy[k];
            if (nx < 0 || nx > air[0].first || ny < 0 || ny >= c || visited[nx][ny] == true)
                continue;
            visited[nx][ny] = true;
            break;
        }
        if (x == air[0].first && y == air[0].second)
        {
            answer -= arr[nx][ny];
            arr[nx][ny] = 0;
        }
        else if (nx == air[0].first && ny == air[0].second)
        {
            arr[x][y] = 0;
            break;
        }
        else
            swapPos(x, y, nx, ny);
        x = nx;
        y = ny;
    }
}

void operateAirDown()
{
    bool visited[50][50];
    int x = air[1].first, y = air[1].second;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (i == x || j == y || i == r - 1 || j == c - 1)
                visited[i][j] = false;
            else
                visited[i][j] = true;
        }
    }
    while (true)
    {
        int dx[4] = {1, 0, -1, 0};
        int dy[4] = {0, 1, 0, -1};
        int nx, ny;
        for (int k = 0; k < 4; k++)
        {
            nx = x + dx[k];
            ny = y + dy[k];
            if (nx < air[1].first || nx >= r || ny < 0 || ny >= c || visited[nx][ny] == true)
                continue;
            visited[nx][ny] = true;
            break;
        }
        if (x == air[1].first && y == air[1].second)
        {
            answer -= arr[nx][ny];
            arr[nx][ny] = 0;
        }
        else if (nx == air[1].first && ny == air[1].second)
        {
            arr[x][y] = 0;
            break;
        }
        else
            swapPos(x, y, nx, ny);
        x = nx;
        y = ny;
    }
}

void    gain() //바꾸는건 arr에 바꾸고 순회는 temp기준으로 할 것
{
    int dx[4] = {1, -1, 0, 0};
    int dy[4] = {0, 0, 1, -1};
    memcpy(temp, arr, sizeof(int) * 50 * 50);

    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            if (temp[i][j] > 0)
            {
                int count = 0;
                int dirty = temp[i][j] / 5;
                for (int k = 0; k < 4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];

                    if (nx < 0 || ny < 0 || nx >= r || ny >= c || temp[nx][ny] == -1)
                        continue;
                    arr[nx][ny] += dirty;
                    answer += dirty;
                    count++;
                }
                arr[i][j] -= dirty * count;
                answer -= dirty * count;
            }
        }
    }
}

int main()
{
    cin >> r >> c >> t;
    for (int i = 0; i < r; i++)
    {
        for (int j = 0; j < c; j++)
        {
            cin >> arr[i][j];
            
            if (arr[i][j] == -1)
                air.push_back(make_pair(i, j));
            else
                answer += arr[i][j];
        }
    }
    while (t > 0)
    {
        gain();
        operateAirDown();
        operateAirUp();
        t--;
    }
    cout << answer;
}