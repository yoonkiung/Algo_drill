#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <string.h>

using namespace std;

vector<vector<long long> > bus;
long long n, m;
long long dis[501];

bool balman(long long start)
{
    long long node = start;

    for (long long i = 1; i <= n; i++)
        dis[i] = 1e9;
    dis[start] = 0;

    for (long long node = 1; node <= n; node++)
    {
        for (long long j = 0; j < bus.size(); j++)
        {
            long long cur = bus[j][0];
            long long next = bus[j][1];
            long long nextDis = bus[j][2];

            if (dis[cur] != 1e9 && dis[next] > dis[cur] + nextDis)
            {
                dis[next] = dis[cur] + nextDis;
                // if (node == n - 1)
                //     return false;
            }
        }
    }
    for (long long node = 1; node <= n; node++)
    {
        for (long long j = 0; j < bus.size(); j++)
        {
            long long cur = bus[j][0];
            long long next = bus[j][1];
            long long nextDis = bus[j][2];

            if (dis[cur] != 1e9 && dis[next] > dis[cur] + nextDis)
            {
                return false;
            }
        }
    }
    return true;
}


int main()
{
    cin >> n >> m;
    for (long long i = 0; i < m; i++)
    {
        long long a, b, c;

        cin >> a >> b >> c;
        bus.push_back({a, b, c});
    }
    if (!balman(1))
        cout << -1;
    else
    {
        for (long long i = 2; i <= n; i++)
        {
            if (dis[i] == 1e9)
                cout << -1 << "\n";
            else
                cout << dis[i] << "\n";
        }
            
    }
}