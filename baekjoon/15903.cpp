#include <iostream>
#include <stdio.h>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    long long int n, m, answer = 0;
    priority_queue<long long int> que;

    cin >> n >> m;
    for (long long int i = 0; i < n; i++)
    {
        long long int temp;
        cin >> temp;
        answer += temp;
        que.push(-temp);
    }
    for (long long int i = 0; i < m; i++)
    {
        long long int a1, a2;
        a1 = que.top() * -1;
        que.pop();
        a2 = que.top() * -1;
        que.pop();
        answer -= a1 + a2;
        que.push((a1 + a2) * -1);
        que.push((a1 + a2) * -1);
        answer += (a1 + a2) * 2;
    }
    cout << answer;
}