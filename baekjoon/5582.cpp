#include <iostream>
#include <vector>
#include <string>
#include <limits.h>

using namespace std;

int maxValue = 0;

int main()
{
    string s1, s2;
    cin >> s1 >> s2;

    vector<vector<int> > lcs(s2.size() + 1, vector<int>(s1.size() + 1, 0));
    for (int i = 0; i < s2.size() + 1; i++)
    {
        for (int j = 0; j < s1.size() + 1; j++)
        {
            if (i == 0 || j == 0)
                continue;
            if (s2[i - 1] == s1[j - 1])
            {
                lcs[i][j] = lcs[i - 1][j - 1] + 1;
                maxValue = max(maxValue, lcs[i][j]);
            }
        }
    }

    cout << maxValue;
}