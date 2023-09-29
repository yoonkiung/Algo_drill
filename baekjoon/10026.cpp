#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>

using namespace std;

int n;
char arr[101][101];
bool visited[101][101] = {false,};
int dx[4] = {1, -1, 0, 0};
int dy[4] = {0, 0, 1, -1};
int answerNormal = 0;
int answerBlind = 0;
char curColor;

void    searchNormal(int x, int y)
{
    visited[x][y] = true;

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[nx][ny] || arr[nx][ny] != curColor)
            continue;        
        visited[nx][ny] = true;
        searchNormal(nx, ny);
    }
}

void    searchBlind(int x, int y)
{
    visited[x][y] = true;

    for (int i = 0; i < 4; i++)
    {
        int nx = x + dx[i];
        int ny = y + dy[i];

        if (nx < 0 || ny < 0 || nx >= n || ny >= n || visited[nx][ny])
            continue;        
        if (curColor == 'R' || curColor == 'G')
        {
            if (arr[nx][ny] == 'R' || arr[nx][ny] == 'G')
            {
                visited[nx][ny] = true;
                searchBlind(nx, ny);
            }
        }
        else
        {
            if (arr[nx][ny] == 'B')
            {
                visited[nx][ny] = true;
                searchBlind(nx, ny);
            }
        }
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < n; i++)
        cin >> arr[i];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                answerNormal++;
                curColor = arr[i][j];
                searchNormal(i, j);
            }
        }
    }
    memset(visited, false, sizeof(visited));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (!visited[i][j])
            {
                answerBlind++;
                curColor = arr[i][j];
                searchBlind(i, j);
            }
        }
    }
    cout << answerNormal << " " << answerBlind;
}