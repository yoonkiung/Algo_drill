#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

bool visited[100001] = {false,};

int main()
{
    int n, k, answer = 100000000;
    queue<pair<int, int> > que;
            //위치, 시간
    cin >> n >> k;
    que.push(make_pair(n, 0));
    visited[n] = true;

    int dx[2] = {1, -1};
    while (!que.empty())
    {
        int x = que.front().first, time = que.front().second;
        // cout << x  << " " << time << "\n";
        que.pop();
        visited[x] = true;
        if (x == k && time < answer)
        {
            answer = time;
            break;
        }
        if (x * 2 >= 0 && x * 2 <= 100000 && visited[x * 2] == false)
            que.push(make_pair(x * 2, time));
        for (int i = 0; i < 2; i++)
        {
            int nx = x + dx[i];
            if (nx < 0 || nx >= 100001 || visited[nx] == true)
                continue;
            que.push(make_pair(nx, time + 1));
        }
    }
    cout << answer;
}