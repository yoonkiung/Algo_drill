#include <iostream>
#include <stdio.h>
#include <vector>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

int main()
{
    int n, m;
    vector<string> vec;
    cin >> n >> m;
    int underBarLen = m;
    for (int i = 0; i < n; i++)
    {
        string temp;
        cin >> temp;
        underBarLen -= temp.length();
        vec.push_back(temp);
    }
    string underBar = "";
    for (int i = 0; i < underBarLen / (n - 1); i++)
        underBar += "_";
    underBarLen = underBarLen % (n - 1);

    string answer = "";
    int spaceNum = vec.size() - 1;
    while (!vec.empty())
    {
        answer += vec.front();
        vec.erase(vec.begin());
        if (vec.empty())
            break;
        if (underBarLen > 0)
        {
            if (spaceNum <= underBarLen || (vec[0][0] >= 'a' && vec[0][0] <= 'z'))
            {
                answer += underBar + "_";
                underBarLen--;
            }
            else
            {
                answer += underBar;    
            }
        }
        else
            answer += underBar;
        spaceNum--;
    }
    cout << answer;
}