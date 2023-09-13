#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int cmp(pair<int, int>p1, pair<int, int> p2)
{
    if (p1.first == p2.first)
        return(p1.second < p2.second);
    return (p1.first < p2.first);
}

int main()
{
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
    int lastEndTime = 0;
    for (vector<pair<int, int> >::iterator iter = vec.begin(); iter != vec.end(); iter++)
    {
        if (lastEndTime <= (*iter).first)
            lastEndTime = (*iter).first + (*iter).second;
        else
            lastEndTime = lastEndTime + (*iter).second;
    }
    cout << lastEndTime;
}