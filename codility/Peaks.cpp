// you can use includes, for example:
// #include <algorithm>
#include <vector>
using namespace std;
// you can write to stdout for debugging purposes, e.g.
// cout << "this is a debug message" << endl;

int solution(vector<int> &A) {
    vector<int> peak;
    int ret = 0;

    for (int i = 1; i < A.size() - 1; i++)
    {
        if (A[i - 1] < A[i] && A[i] > A[i + 1])
            peak.push_back(i);
    }

    if (peak.size() == 0)
        return 0;

    for (int i = A.size(); i >= 1; i--)
    {
        if (A.size() % i != 0)
            continue;
        
        bool success = true;
        int start = 0;
        int last = start + (A.size() / i) - 1;

        for (int p : peak)
        {
            if (start <= p && p <= last)
            {
                start += (A.size() / i);
                last = start + (A.size() / i) - 1;

                if (start == A.size())
                    break;
            }
            else if (p < start)
                continue;
            else if (p > last)
            {
                success = false;
                break;
            }
            
        }

        if (!success || start != A.size())
            continue;
        ret = i;
        break;
        
    }
    return ret;
}