#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int n, m, answer = 0;
    vector<int> vec;

    cin >> n >> m;
    for (int i = 0; i < n; i++)
    {
        int temp;
        cin >> temp;
        vec.push_back(temp);
    }
    sort(vec.begin(), vec.end());
    if (vec[0] * vec[n - 1] > 0) //다 같을 경우
    {
        if (vec[0] > 0) // 양수만으로 이뤄질경우
        {
            answer += vec.back();
            for (int i = 0; i < m; i++)
            {
                if (vec.empty())
                    break;
                vec.pop_back();
            }
            while (vec.size() > 0)
            {
                answer += vec.back() * 2;
                for (int i = 0; i < m; i++)
                {
                    if (vec.empty())
                        break;
                    vec.pop_back();
                }   
            }
        }
        else // 음수로만 이뤄질경우
        {
            answer += vec.front() * (-1);
            for (int i = 0; i < m; i++)
            {
                if (vec.empty())
                    break;
                vec.erase(vec.begin());
            }
            while (vec.size() > 0)
            {
                answer += vec.front() * (-2);
                for (int i = 0; i < m; i++)
                {
                    if (vec.empty())
                        break;
                    vec.erase(vec.begin());
                }
            }
        }
    }
    else //혼합되어있을경우
    {
        if (abs(vec[0]) > vec[n - 1]) // 음수쪽이 더 멀 경우
        {
            while (vec.back() > 0)
            {
                answer += vec.back() * 2;
                for (int i = 0; i < m; i++)
                {
                    if (vec.back() < 0)
                        break;
                    vec.pop_back();
                }
            }
            answer += vec.front() * (-1);
            for (int i = 0; i < m; i++)
            {
                if (vec.empty())
                    break;
                vec.erase(vec.begin());
            }
            while (vec.size() > 0)
            {
                answer += vec.front() * (-2);
                for (int i = 0; i < m; i++)
                {
                    if (vec.empty())
                        break;
                    vec.erase(vec.begin());
                }
            }
        }
        else //양수쪽이 더 멀 경우
        {
            while (vec.front() < 0)
            {
                answer += vec.front() * (-2);
                for (int i = 0; i < m; i++)
                {
                    if (vec.front() > 0)
                        break;
                    vec.erase(vec.begin());
                }
            }
            answer += vec.back();
            for (int i = 0; i < m; i++)
            {
                if (vec.empty())
                    break;
                vec.pop_back();
            }
            while (vec.size() > 0)
            {
                answer += vec.back() * 2;
                for (int i = 0; i < m; i++)
                {
                    if (vec.empty())
                        break;
                    vec.pop_back();
                }   
            }
        }
    }
    cout << answer;
}