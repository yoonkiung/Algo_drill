#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

long long int days[10000001] = {0,};

int main()
{
    std::cin.tie(0);
    std::cout.tie(0);
    std::ios_base::sync_with_stdio(false);
    long long int t, n;

    cin >> t;
    
    for (long long int z = 0; z < t; z++)
    {
        long long int answer = 0, max = 0;
        cin >> n;
        for (long long int i = 0; i < n; i++)
            cin >> days[i + 1];
        while (n >= 1)
        {
            if (days[n] >= max)
                max = days[n];
            else
                answer += max - days[n];
            n--;
        }
        cout << answer << "\n";
    }
}