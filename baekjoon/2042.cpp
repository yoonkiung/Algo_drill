#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

long long arr[1000001];
long long tree[4000001];

long long make_tree(long long node, long long left, long long right)
{
    if (left == right)
        return tree[node] = arr[left];
    
    long long mid = (left + right) / 2;

    return tree[node] = make_tree(node * 2, left, mid) + make_tree(node * 2 + 1, mid + 1, right);    
}

void update(long long node, long long left, long long right, const long long& newIndex, const long long& newValue)
{
    if (left == right)
    {
        tree[node] = newValue;
        return ;
    }
    long long mid = (left + right) / 2;

    if (left <= newIndex && newIndex <= mid)
        update(node * 2, left, mid, newIndex, newValue);
    else
        update(node * 2 + 1, mid + 1, right, newIndex, newValue);
    
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
    return ;
}

long long sum(long long node, long long left, long long right, const long long& b, const long long& c)
{
    if (c < left || right < b)
        return 0;

    if (b <= left && right <= c)
        return tree[node];
    
    long long mid = (left + right) / 2;

    return sum(node * 2, left, mid, b, c) + sum(node * 2 + 1, mid + 1, right, b, c);    
}

int main()
{
    long long n, m, k;

    cin >> n >> m >> k;
    for (long long i = 0; i < n; i++)
        cin >> arr[i];
    make_tree(1, 0, n - 1);
    for (long long i = 0; i < m + k; i++)
    {
        long long a, b, c;

        cin >> a >> b >> c;
        if (a == 1)
            update(1, 0, n - 1, b - 1, c);
        else
            cout << sum(1, 0, n - 1, b - 1, c - 1) << "\n";
    }
}