#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    long long int n, answer = 0;
    vector<long long int> trees;
    vector<long long int> growth;
    priority_queue<pair<int, int> > que;

    cin >> n;
    for (long long int i = 0; i < n; i++)
    {
        long long int temp;
        cin >> temp;
        trees.push_back(temp);
    }
    for (long long int i = 0; i < n; i++)
    {
        long long int temp;
        cin >> temp;
        growth.push_back(temp);
        que.push(make_pair(-growth[i], trees[i]));
    }
    for (long long int i = 0; i < n; i++)
    {
        answer += -que.top().first * i + que.top().second;
        que.pop();
    }
    cout << answer;
}