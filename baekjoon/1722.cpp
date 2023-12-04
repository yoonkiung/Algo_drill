#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

/*
순열은 정렬할 수 있따. 
k가 주어지면 k번째 순열을 주어지면 k번째 순열을 구하고
임의의 순열이 주어지면 이 순열이 몇 번째 순열인지 출력
*/

vector<long long> vec;

vector<long long> arr = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20};

void    getPermu(long long fact, long long n, long long k)
{
    if (fact == 1)
    {
        vec.push_back(arr[k]);
        return ;
    }        
    else
    {
        fact /= n;
        vec.push_back(arr[k  / fact]);
        arr.erase(arr.begin() + (k  / fact));
        getPermu(fact, n - 1, k % fact);
    }    
}

int main()
{
    long long n, problem;    
    long long all_num = 1;
    
    cin >> n >> problem;
    for (int i = 1; i <= n; i++)
        all_num *= i;
    if (problem == 1)
    {
        long long k;

        cin >> k;
        getPermu(all_num, n, k - 1);
        for (int v : vec)
            cout << v << " ";
    }
    else
    {
        long long ret = 0;
        int temp = n;
        for (int j = 0; j < temp; j++)
        {
            long long num;

            cin >> num;
            auto it = find(arr.begin(), arr.end(), num);
            if (n > 0)
                all_num /= n;
            n--;
            ret += (it - arr.begin()) * all_num;
            arr.erase(it);
        }
        cout << ret + 1;
    }
}
