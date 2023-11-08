#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int L[201] = {0,};
int P[201] = {0,};
int inc[10];
int main()
{
    int len = 0;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int cur;
        cin >> cur;

        auto pos = lower_bound(L, L + len + 1, cur);
        *pos = cur;
        P[i] = distance(L, pos);
        if (pos == L + len + 1)
            len++;
        
    }
    for (int i = 0; i < 10; i++)
    {
        cout << P[i] << " ";
    }
    cout << "\n";
    cout << n - len;
}

