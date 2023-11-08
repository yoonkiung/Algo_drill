#include <iostream>
#include <vector>
#include <string>
#include <string.h>

using namespace std;

int n;
int arr[101];
long long answer[21] = {0,};

int main()
{
    int num; 
    cin >> n;
    cin >> num;
    answer[num] = 1;
    for (int i = 0; i < n - 2; i++)
    {
        long long temp[21];
        memset(temp, 0, sizeof(temp));
        cin >> num;
        for (int j = 0; j <= 20; j++)
        {
            if (answer[j] != 0)
            {
                if (j - num >= 0)
                    temp[j - num] += answer[j];
                if (j + num <= 20)
                    temp[j + num] += answer[j];
            }
        }
        memcpy(answer, temp, sizeof(temp));
    }
    cin >> num;
    cout << answer[num];
    return 0;
}