#include <iostream>
#include <queue>
#include <algorithm>
#define MAX 300001

using namespace std;

int main()
{
    long long n, k, answer = 0;
    pair<long long, long long> jew[MAX];
    long long bags[MAX];
    priority_queue<long long> que;

    cin >> n >> k;
    for (long long i = 0; i < n; i++)
    {
        long long weight, price;
        cin >> weight >> price;
        jew[i] = make_pair(weight, price);
    }
    for (long long i = 0; i < k; i++)
        cin >> bags[i];
    sort(jew, jew + n);
    sort(bags, bags + k);
    long long idx = 0;
    for (long long i = 0; i < k; i++)
    {
        while (idx < n)
        {
            if (bags[i] < jew[idx].first)
                break;
            que.push(jew[idx].second);
            idx++;
        }
        if (!que.empty())
        {
            answer += que.top();
            que.pop();
        }
    }
    cout << answer;
}