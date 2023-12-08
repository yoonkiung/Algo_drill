#include <iostream>
#include <vector>
#include <string>
#include <limits.h>
#include <string.h>

using namespace std;

int n, m;
int board[1000001];

int find(int a)
{
    if (a == board[a])
        return a;
    return board[a] = find(board[a]);
}

void    uni(int a, int b)
{
    a = find(a);
    b = find(b);
    if (a == b)
        return ;
    board[a] = b;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    for (int i = 1; i <= n; i++)
        board[i] = i;
    for (int i = 0; i < m; i++)
    {
        int cmd, a, b;

        cin >> cmd >> a >> b;
        if (cmd == 0)
        {
            uni(a, b);
        }
        else
        {
            a = find(a);
            b = find(b);
            if (a == b)
                cout << "YES\n";
            else
                cout << "NO\n";
        }
    }
}
