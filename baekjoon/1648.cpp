#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <limits.h>
#include <string.h>

using namespace std;

int n, m;
int cache[14 * 14][1 << 14];

int dfs(int k, int bit)
{
    if (k == n * m)
        return bit == 0;
    
    int& ret = cache[k][bit];
    if (ret != -1)
        return ret;
    ret = 0;

    //현재 칸이 이미 차 있는 경우
    if ((bit & 1) == 1)
        ret += dfs(k + 1, bit >> 1);
    else
    {
        // 2 * 1 블럭 놓는 경우
        ret += dfs(k + 1, (bit >> 1) | (1 << (m - 1)));
        // 1 * 2 블럭 놓는 경우
        if (k % m != m - 1 && (bit & 2) == 0)
            ret += dfs(k + 2, bit >> 2);
    }
    return ret % 9901;
}

int main()
{
    cin >> n >> m;
    memset(cache, -1, sizeof(cache));
    cout << dfs(0, 0);
}