#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int x, answer = 0;

    cin >> x;
    while (x > 0)
    {
        if (x & 0b1){
            answer++;
        }
        x = x >> 1;
    }
    cout << answer;
}