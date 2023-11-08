#include <iostream>
#include <vector>
#include <algorithm>
#include <limits.h>

using namespace std;

int n;
int answer = INT_MAX;
int board[16][16];
bool visited[16] = {false,};

void    dfs(int pos, int cost, int depth)
{
    // cout << pos << " ";
    if (depth == n - 1)
    {
        
        if (board[pos][0] != 0)
        {
            answer = min(answer, cost + board[pos][0]);
            // cout << 0 << " ";
        }   
        // cout << "\n";
        return;
    }
    for (int next = 1; next < n; next++)
    {
        if (visited[next] == true)
            continue;
        if (board[pos][next] == 0)
            continue;
        visited[next] = true;
        dfs(next, cost + board[pos][next], depth + 1);
        visited[next] = false;
        // if (!visited[next] && board[pos][next] != 0)
        // {
        //     visited[next] = true;
        //     dfs(next, cost + board[pos][next], depth + 1);
        //     visited[next] = false;
        // }
    }
}

int main()
{
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
            cin >> board[i][j];
    }
    visited[0] = true;
    dfs(0, 0, 0);
    cout << answer;
}