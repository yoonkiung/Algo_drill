#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int cmp(pair<int, int> p1, pair<int, int> p2)
{
    if (p1.first == p2.first)
        return (p1.second > p2.second);
    return (p1.first < p2.first);
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);

    int n, answer = 0;
    //    <deadline, cup>
    vector<pair<int, int> > vec;
    priority_queue<int, vector<int>, greater<int> > pq;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int deadline, cup;
        
        cin >> deadline >> cup;
        vec.push_back(make_pair(deadline, cup));
        
    }
    sort(vec.begin(), vec.end(), cmp);

    for (vector<pair<int, int> >::iterator iter = vec.begin(); iter != vec.end(); iter++)
    {
        int deadline = (*iter).first;
        int cup = (*iter).second;

        if (pq.size() < deadline)
        {
            answer += cup;
            pq.push(cup);
        }
        else if (pq.top() <= cup)
        {
            answer -= pq.top();
            answer += cup;
            pq.pop();
            pq.push(cup);
        }
    }
    cout << answer;
    for (vector<pair<int, int> >::iterator iter = vec.begin(); iter != vec.end(); iter++)
    {
        int deadline = (*iter).first;
        int cup = (*iter).second;

        if (pq.size() < deadline)
        {
            answer += cup;
            pq.push(cup);
        }
        else if (pq.top() <= cup)
        {
            answer -= pq.top();
            answer += cup;
            pq.pop();
            pq.push(cup);
        }
    }
    cout << answer;
}