#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

bool alph[26] = {false,};
int n, k, answer = 0;
char    word[50][16];

void    countReadable()
{
    int count = 0;
    for (int i = 0; i < n; i++)
    {
        int j = 0;
        bool flag = true;
        while (word[i][j])
        {
            if (!alph[word[i][j] - 'a'])
            {
                flag = false;
                break;
            }
            j++;
        }
        if (flag)
            count++;
    }
    answer = max(answer, count);
}

void    makeCombi(int idx, int selectedCount)
{
    if (selectedCount == k)
    {
        countReadable();
        return ;
    }
    for (int i = idx; i < 26; i++)
    {
        if (alph[i])
            continue;
        alph[i] = true;
        makeCombi(i, selectedCount + 1);
        alph[i] = false;
    }
}


int main()
{
    cin >> n >> k;
    if (k < 5)
    {
        cout << 0;
        return 0;
    }
    for (int i = 0; i < n; i++)
        cin >> word[i];
    alph['a' - 'a'] = true;
    alph['n' - 'a'] = true;
    alph['t' - 'a'] = true;
    alph['i' - 'a'] = true;
    alph['c' - 'a'] = true;
    makeCombi(0, 5);
    cout << answer;
}