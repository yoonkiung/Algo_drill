#include <iostream>
#include <stdio.h>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int main()
{
    string str;
    int index = 1;

    cin >> str;
    while (str.compare(0, 1, "-") != 0)
    {
        stack<char> stk;
        int openCnt = 0;
        int answer = 0;
        for (int i = 0; i < str.length(); i++)
        {
            if (str[i] == '{')
            {
                stk.push(str[i]);
                openCnt++;
            }
            else if (str[i] == '}')
            {
                if (stk.empty() || stk.top() != '{')
                {
                    stk.push('{');
                    openCnt++;
                    answer++;
                }
                else 
                {
                    stk.pop();
                    openCnt--;
                }
            }
        }
        answer += openCnt / 2;
        cout << index++ << ". " << answer << "\n";
        cin >> str;
    }
}