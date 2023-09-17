#include <iostream>
#include <queue>
#include <algorithm>
#include <string>

using namespace std;

int main()
{
    int n, k, answer = 0;
    string str;

    cin >> n >> k;
    cin >> str;

    for (int i = 0; i < n; i++)
    {
        if (str[i] == 'P')
        {
            int startPos = i - k;
            while (startPos <= i + k)
            {
                if (startPos < 0)
                    startPos++;
                else if (startPos >= n)
                    break;
                else if (str[startPos] == 'H')
                {
                    answer++;
                    str[startPos] = '0';
                    break;
                }
                else
                    startPos++;
            }
        }
    }
    cout << answer;
}