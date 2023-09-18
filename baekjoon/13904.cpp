
#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int cmp(pair<int, int> p1, pair<int, int> p2)
{
    return (p1.first < p2.first);
}

int main()
{
    int n, answer = 0;
    cin >> n;
    vector<pair<int, int> > vec;
    priority_queue<int, vector<int>, greater<int> > que;

    for (int i = 0; i < n; i++)
    {
        int d, w;
        cin >> d >> w;
        vec.push_back(make_pair(d, w));
    }
    sort(vec.begin(), vec.end(), cmp);
    for (int i = 0; i < n; i++)
    {
        int d = vec[i].first, w = vec[i].second;
        if (que.size() < d)
            que.push(w);
        else
        {
            if (que.top() < w)
            {
                que.pop();
                que.push(w);
            }
        }
    }
    while (!que.empty())
    {
        answer += que.top();
        // cout << que.top() << "\n";
        que.pop();
    }
    cout << answer;
}