#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int cmp(pair<int, int> p1, pair<int, int> p2)
{
    if (p1.second == p2.second)
        return (p1.first < p2.first);
    return (p1.second < p2.second);
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);
    int n;
    vector<pair<int, int> > vec;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int start, end;
        cin >> start >> end;
        vec.push_back(make_pair(start, end));
    }
    sort(vec.begin(), vec.end(), cmp);
    vector<pair<int, int> >::iterator iter = vec.begin();
    int lastEndTime = 0;
    int count = 0;
    while (iter != vec.end())
    {
        if ((*iter).first >= lastEndTime)
        {
            count++;
            lastEndTime = (*iter).second;
        }
        iter++;
    }
    cout << count;
}