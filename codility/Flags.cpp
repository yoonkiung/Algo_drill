// you can use includes, for example:
// #include <algorithm>
#include <vector>
#include <cmath>
#include <iostream>

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
    if (peak.size() == 1)
        return 1;
    for (int diff = (int)sqrt(400000); diff >= 1; diff--)
    {
        int count = 1;
        int last = peak[0];
        bool success = false;

        for (int i = 1; i < peak.size(); i++)
        {
            if (peak[i] - last >= diff)
            {
                count++;
                last = peak[i];
                if (count == diff)
                {
                    success = true;
                    ret = diff;
                    break;
                }
            }
        }
        if (success)
            break;
    }
    return ret;
}