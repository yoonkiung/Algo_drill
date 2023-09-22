#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int parentIdx;
int n, deleteIdx, answer = 0;
vector<pair<int, vector<int> > > tree(50);
//         <parent, childList>

void bfs()
{
    queue<int> que;

    if (parentIdx != deleteIdx)
        que.push(parentIdx);
    while (!que.empty())
    {
        int curIndex = que.front();
        que.pop();
        if (tree[curIndex].second.size() == 0 && tree[curIndex].first != -1)
            answer++;
        else
        {
            for (auto o : tree[curIndex].second)
            {
                if (o == deleteIdx)
                {
                    if (tree[curIndex].second.size() == 1)// && tree[curIndex].first != -1)
                        answer++;
                    continue;
                }
                else        
                    que.push(o);
            }
        }
    }
}

int main()
{
    cin >> n;    
    for (int i = 0; i < n; i++)
    {
        int parent;

        cin >> parent;
        tree[i].first = parent;
        if (parent == -1)
        {
            parentIdx = i;
            continue;
        }            
        tree[parent].second.push_back(i);
    }
    cin >> deleteIdx;
    bfs();
    cout << answer;
    
    // for (auto o : tree)
    // {
    //     cout << "parent : " << o.first << " child : ";
    //     for (auto a : o.second)
    //         cout << a << " ";
    //     cout << "\n";
    // }
    return (0);
    
}