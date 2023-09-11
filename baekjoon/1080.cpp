#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int n, m;
vector<string> vec;
vector<string> ans;

int isSame()
{
    for (int i = 0; i < n; i++)
    {
        if (vec[i].compare(ans[i]) != 0)
            return 0;
    }
    return 1;
}

void    convert(int x, int y)
{
    for (int i = x; i < x + 3; i++)
    {
        for (int j = y; j < y + 3; j++)
        {
            if (vec[i][j] == '0')
                vec[i][j] = '1';
            else
                vec[i][j] = '0';
        }
    }
}

int main()
{
    int answer = 0;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        vec.push_back(temp);
    }
    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        ans.push_back(temp);
    }

    if (n < 3 || m < 3)
    {
        if (isSame())
            cout << 0;
        else
            cout << -1;
    }
    else
    {
        for (int i = 0; i < n - 2; i++)
        {
            for (int j = 0; j < m - 2; j++)
            {
                if (vec[i][j] != ans[i][j])
                {
                    convert(i, j);
                    answer++;
                }    
            }
        }
        if (isSame())
            cout << answer;
        else
            cout << -1;
    }
}