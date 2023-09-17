#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    int n;
    double arr[7];
    cin >> n;
    priority_queue<double> que;

    for (int i= 0; i < n; i++)
    {
        double tmp;
        cin >> tmp;

        if (que.size() < 7)
            que.push(tmp);
        else if (que.top() > tmp)
        {
            que.pop();
            que.push(tmp);
        }
    }
    for (int i = 0; i < 7; i++)
    {
        arr[i] = que.top();
        que.pop();
    }
    for (int i = 6; i >= 0; i--)
        printf("%.3lf\n", arr[i]);
}