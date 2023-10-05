#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
#include <limits.h>
#include <string.h>
#include <string>

using namespace std;

int n, answer = INT_MAX;
int arr[15][5];
int limit[4];
bool selected[15] = {false,};
int full = 0;
bool selectedSet[15] = {false,};
bool findFlag = false;
//단백질     0
//지방      1
//탄수화물   2
//비타민    3

void    makeCombi(int idx, int selectCount)
{
    if (selectCount == full)
    {
        int n0 = 0, n1 = 0, n2 = 0, n3 = 0, price = 0;
        for (int i = 0; i < n; i++)
        {
            if (selected[i])
            {
                n0 += arr[i][0];
                n1 += arr[i][1];
                n2 += arr[i][2];
                n3 += arr[i][3];
                price += arr[i][4];
            }
            if (n0 >= limit[0] && n1 >= limit[1] && n2 >= limit[2] && n3 >= limit[3])
            {
                if (answer > price)
                {
                    findFlag = true;
                    answer = price;
                    // memset(selectedSet, false, sizeof(selectedSet));
                    memcpy(selectedSet, selected, sizeof(selected));
                }     
                else if (answer == price)
                {
                    vector<int> ex;
                    vector<int> next;
                    bool changeFlag = true;
                    for (int j = 0; j < n; j++)
                    {
                        if (selectedSet[j])
                            ex.push_back(j + 1);
                        if (selected[j])
                            next.push_back(j + 1);
                    }
                    int j = 0;
                    while (j < n)
                    {
                        if (ex.size() == j && next.size() > j)
                        {
                            changeFlag = false;
                            break;
                        }
                        else if (ex.size() > j && next.size() == j)
                        {
                            // changeFlag = false;
                            break;
                        }
                        else if (ex.size() == j && next.size() == j)
                            break;
                        else if (next[j] > ex[j])
                        {
                            changeFlag = false;
                            break;
                        }
                        else if (next[j] < ex[j])
                            break;
                        j++;
                    }
                    if (changeFlag)
                        memcpy(selectedSet, selected, sizeof(selected));
                }
            }
        }
    }
    for (int i = idx; i < n; i++)
    {
        if (!selected[i])
        {
            selected[i] = true;
            makeCombi(i, selectCount + 1);
            selected[i] = false;
        }
    }
}

int main()
{
    cin >> n;
    for (int i = 0; i < 4; i++)
        cin >> limit[i];
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < 5; j++)
            cin >> arr[i][j];
    }
    for (int i = 1; i <= n; i++)
    {
        full = i;
        memset(selected, false, sizeof(selected));
        makeCombi(0, 0);
    }
    if (findFlag)
    {
        cout << answer << "\n";
        for (int i = 0; i < n; i++)
        {
            if (selectedSet[i])
                cout << i + 1 << " ";
        }
    }
    else
    {
        cout << -1;
    }
    
}