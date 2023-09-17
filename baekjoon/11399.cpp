#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int n, answer = 0;
    cin >> n;
    vector<int> vec;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    for (int i = 0; i < n; i++)
        answer += (n - i) * vec[i];
    cout << answer;
}