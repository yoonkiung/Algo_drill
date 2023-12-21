#include <iostream>
#include <vector>
#include <algorithm>
#include <iostream>
#include <unordered_map>

using namespace std;

unordered_map <string, string> relation;
unordered_map <string, int> amount;


string find(string a)
{
    if (relation[a] == a)
        return a;
    return relation[a] = find(relation[a]);
}

void    uni(string a, string b)
{
    int ret;

    if (relation.find(a) == relation.end() && relation.find(b) == relation.end())
    {
        relation[a] = a;
        relation[b] = a;
        amount[a] = 2;
        amount[b] = 2;
        ret = 2;
    }
    else if (relation.find(a) == relation.end())
    {
        b = find(b);
        relation[a] = b;
        amount[b] += 1;
        ret = amount[b];
    }
    else if (relation.find(b) == relation.end())
    {
        a = find(a);
        relation[b] = a;
        amount[a]++;
        ret = amount[a];
    }
    else
    {
        a = find(a);
        b = find(b);
        if (a == b)
            ret = amount[a];
        else
        {
            ret = amount[a] + amount[b];
            if (amount[a] > amount[b])
            {
                amount[a] += amount[b];
                relation[b] = a;
            }
            else
            {
                amount[b] += amount[a];
                relation[a] = b;
            }
        }
    }
    cout << ret << "\n";
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;

    cin >> t;
    for (int i = 0; i < t; i++)
    {
        int f;
        
        cin >> f;
        relation.clear();
        amount.clear();
        for (int j = 0; j < f; j++)
        {
            string a, b;
            
            cin >> a >> b;
            uni(a, b);
        }
    }
}