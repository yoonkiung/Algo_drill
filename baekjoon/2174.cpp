#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

unordered_map<int, pair<vector<int>, char> > um;
int board[101][101];

vector<int> findDelta(char c)
{
    if (c == 'N')
        return {0, 1};
    if (c == 'S')
        return {0, -1};
    if (c == 'W')
        return {-1, 0};    
    else
        return {1, 0};
}

char    rotateLeft(char c)
{
    if (c == 'N')
        return 'W';
    if (c == 'S')
        return 'E';
    if (c == 'W')
        return 'S';    
    else
        return 'N';
}

char    rotateRight(char c)
{
    if (c == 'N')
        return 'E';
    if (c == 'S')
        return 'W';
    if (c == 'W')
        return 'N';    
    else
        return 'S';
}

int main()
{
    int n, m;
    int a, b;
    cin >> n >> m >> a >> b;
    
    for (int i = 0; i < a; i++)
    {
        int x, y;
        char d;

        cin >> x >> y >> d;
        um[i + 1] = {{x, y}, d};
        board[x][y] = i + 1;
    }
    for (int i = 0; i < b; i++)
    {
        int robot, loop;
        char command;

        cin >> robot >> command >> loop;
        if (command == 'L')
        {
            loop %= 4;
            while (loop > 0)
            {
                um[robot].second = rotateLeft(um[robot].second);
                loop--;
            }
        }
        else if (command == 'R')
        {
            loop %= 4;
            while (loop > 0)
            {
                um[robot].second = rotateRight(um[robot].second);
                loop--;
            }
        }
        else
        {
            while (loop > 0)
            {
                vector<int> cur = um[robot].first;
                vector<int> delta = findDelta(um[robot].second);
                int nx = cur[0] + delta[0];
                int ny = cur[1] + delta[1];
                // cout << cur[0] << " " << cur[1] << " " << nx << " " << ny << "\n";
                if (nx < 1 || nx >= n + 1 || ny < 1 || ny >= m + 1)
                {
                    cout << "Robot " << robot << " crashes into the wall";
                    return 0;
                }
                if (board[nx][ny] != 0)
                {
                    cout << "Robot " << robot << " crashes into robot " << board[nx][ny];
                    return 0;
                }
                board[cur[0]][cur[1]] = 0;
                board[nx][ny] = robot;
                um[robot].first = {nx, ny};
                loop--;
            }
        }
    }
    cout << "OK";
    return 0;
}