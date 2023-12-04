#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int board[201];


int find(int a)
{
    if (board[a] == a)
        return a;
    return board[a] = find(board[a]);
}

void uni(int a, int b)
{
    a = find(a);
    b = find(b);

    if (a != b)
        board[a] = b;
}

int main()
{
    int n, m;

    cin >> n >> m;
    for (int i = 0; i < 201; i++)
        board[i] = i;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int isConnect;

            cin >> isConnect;
            if (isConnect)
                uni(i + 1, j + 1);
        }
    }   

    int root = -1; 
    for (int i = 0; i < m; i++)
    {
        int city;

        cin >> city;
        if (root == -1)
            root = find(city);
        else if (find(city) != root)
        {
            cout << "NO";
            return 0;
        }           
    }
    cout << "YES";
    return 0;
}