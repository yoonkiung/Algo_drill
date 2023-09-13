#include <iostream>
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int days[10001] = {0,};

int cmp(pair<int, int> p1, pair<int, int> p2)
{
    if (p1.first == p2.first)
        return (p1.second < p2.second);
    return (p1.first > p2.first);
}

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);   
    int n, answer = 0;
    // <pay, deadline>
    vector<pair<int, int> > vec;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int pay, deadline;
        cin >> pay >> deadline;
        vec.push_back(make_pair(pay, deadline));
    }
    sort(vec.begin(), vec.end(), cmp);
    
    vector<pair<int, int> >::iterator iter = vec.begin();
    while (iter != vec.end())
    {
        int pay = (*iter).first;
        int deadline = (*iter).second;

        while (deadline >= 1)
        {
            if (days[deadline] == 0)
            {
                days[deadline] = pay;
                answer += pay;
                break;
            }
            deadline--;
        }
        iter++;
    }
    cout << answer;
}

/*
1   2   3   3   3
2   2   100 100 100

3   3   3   1   2
100 100 100 2   2
*/