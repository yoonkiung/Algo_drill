#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int cmp(string s1, string s2)
{
    return s1.length() < s2.length();
}

int main()
{
    int n, count;
    vector<string> vec;
    cin >> n;

    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        vec.push_back(temp);
    }

    sort(vec.begin(), vec.end(), cmp);
    count = n;
    for (int i = 0; i < n - 1; i++)
    {
        int firstLen = vec[i].length();
        for (int j = i + 1; j < n; j++)
        {
            if (!vec[j].compare(0, firstLen, vec[i]))
            {
                count--;
                break;
            }
        }
    }
    cout << count;
}