#include <iostream>
#include <queue>
#include <algorithm>

using namespace std;

int main()
{
    int n, k, answer = 0;
    vector<int> vec, multiTap;
    int arr[101] = {0,};

    cin >> n >> k;
    for (int i = 0; i < k; i++)
    {
        int temp;
        cin >> temp;
        vec.push_back(temp);
        arr[temp]++;
    }
    for (int i = 0; i < k; i++)
    {
        if (find(multiTap.begin(), multiTap.end(), vec[i]) != multiTap.end())
            continue;
        else if (multiTap.size() < n)
            multiTap.push_back(vec[i]);
        else
        {
            if (find(multiTap.begin(), multiTap.end(), vec[i]) == multiTap.end())
            {
                vector<int>::iterator lastIdx = vec.begin();
                int changeIdx = 0;
                for (int j = 0; j < multiTap.size(); j++)
                {
                    vector<int>::iterator it = find(vec.begin() + i + 1, vec.end(), multiTap[j]);
                    if (it == vec.end())
                    {
                        changeIdx = j;
                        break;
                    }
                    else if (lastIdx < it)
                    {
                        lastIdx = it;
                        changeIdx = j;
                    }
                }
                answer++;
                multiTap[changeIdx] = vec[i];
            }
        }
    }
    cout << answer;
}