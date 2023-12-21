#include <iostream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <string.h>
#include <queue>

using namespace std;

long long arr[100000];
pair<long long, long long> tree[400001];
//{최소, 최대}
void    make_tree(long long node, long long left, long long right)
{
    if (left == right)
    {
        tree[node].first = arr[left];
        tree[node].second = arr[left];
        return;
    }
    long long mid = (left + right) / 2;
    make_tree(node * 2, left, mid);
    make_tree(node * 2 + 1, mid + 1, right);
    tree[node].first = min(tree[node * 2].first, tree[node * 2 + 1].first);
    tree[node].second = max(tree[node * 2].second, tree[node * 2 + 1].second);
}

pair<long long, long long> query(long long node, long long left, long long right, const long long& a, const long long& b)
{
    if (b < left || right < a)
        return {-1, -1};
    if (a <= left && right <= b)
        return tree[node];
    long long mid = (left + right) / 2;
    pair<long long, long long> l = query(node * 2, left, mid, a, b);
    pair<long long, long long> r = query(node * 2 + 1, mid + 1, right, a, b);
    if (l.first == -1)
        return r;
    if (r.first == -1)
        return l;
    return {min(l.first, r.first), max(l.second, r.second)};
}

int main()
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    cout.tie(0);
    long long n, m;

    cin >> n >> m;
    for (long long i = 0; i < n; i++)
        cin >> arr[i];
    make_tree(1, 0, n - 1);
    // for (long long i = 1; i < 4 * n + 1; i++)
    //     cout << tree[i].first  << " " << tree[i].second << "\n";
    for (long long i = 0; i < m; i++)
    {
        long long a, b;

        cin >> a >> b;

        pair<long long, long long> ans = query(1, 0, n - 1, a - 1, b - 1);
        cout << ans.first << " " << ans.second << "\n";
    }   
}