#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n, answer = 0;
    vector<int> vec;

    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;    
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    while (vec.size() > 2)
    {
        answer++;
        if (vec.front() == 1)
        {
            int newChain = 0;
            vec.erase(vec.begin());
            newChain += vec.back();
            vec.pop_back();
            newChain += vec.back();
            vec.pop_back();
            vec.push_back(newChain + 1);
        }
        else
        {
            int newChain = 0;
            vec[0] -= 1;
            newChain += vec.back();
            vec.pop_back();
            newChain += vec.back();
            vec.pop_back();
            vec.push_back(newChain + 1);
        }
    }
    if (vec.size() == 2)
        answer++;
    cout << answer;
}