#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

int n, k, answer = 0, lessTime = 100001;
bool visited[100001] = {false,};

int main()
{    
    cin >> n >> k;
    queue<pair<int, int> > que;
    //         좌표, depth
    que.push(make_pair(n, 0));
    // visited[n] = true;
    while (!que.empty())
    {
        int dx[2] = {1, -1};
        int x = que.front().first, depth = que.front().second;
        visited[x] = true;
        que.pop();
        if (x == k)
        {
            if (lessTime == 100001)
            {
                answer++;
                lessTime = depth;
            }
            else
                if (depth == lessTime)
                    answer++;
        }
        else
        {
            int nx = x * 2;
            if (nx >= 0 && nx < 100001 && visited[nx] == false)
            {
                que.push(make_pair(nx, depth + 1));
                // visited[nx] = true;
            }
            for (int i = 0; i < 2; i++)
            {
                nx = x + dx[i];
                if (nx >= 0 && nx < 100001 && visited[nx] == false)
                {
                    que.push(make_pair(nx, depth + 1));
                    // cout << nx << " " <<depth + 1 << endl;
                    // visited[nx] = true;
                }
            }
        }
    }
    
    cout << lessTime << " " <<answer;
}