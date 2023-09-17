#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int par[100001];

int uni(int idx)
{
    if (idx == par[idx])
        return idx;
    return par[idx] = uni(par[idx]);
}

int main()
{
    int g, p, answer = 0;;
    for (int i = 0; i < 100001; i++)
        par[i] = i;
    cin >> g >> p;
    for (int i = 0; i < p; i++)
    {
        int plane;
        cin >> plane;

        int doc = par[plane] = uni(plane);
        if (doc == 0)
            break;
        answer++;
        par[doc] = uni(par[doc - 1]);
    }
    cout << answer;
}