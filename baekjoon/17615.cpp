#include <iostream>
#include <queue>
#include <algorithm>
#include <string.h>

using namespace std;

void swap(char *str, int pos1, int pos2)
{
    char temp = str[pos1];

    str[pos1] = str[pos2];
    str[pos2] = temp;
}

int move(char *str, char word)
{
    int i = 0, savePos = 0, leftAnswer = 0;
    int strLen = strlen(str);
    char saveStr[500005];
    strcpy(saveStr, str);
    while (i < strLen)
    {
        if (str[i] != word)
        {
            if (i == 0 || str[i] != str[i - 1])
                savePos = i;    
        }
        else
        {
            if (savePos != i)
            {
                swap(str, savePos, i);
                leftAnswer++;
            }
            savePos++;
        }
        i++;
    }
    strcpy(str, saveStr);
    i = strLen - 1;
    savePos = i;
    int rightAnswer = 0;
    while (i >= 0)
    {
        if (str[i] != word)
        {
            if (i == strLen - 1 || str[i] != str[i + 1])
                savePos = i;
        }
        else
        {
            if (savePos != i)
            {
                swap(str, savePos, i);
                rightAnswer++;
            }
            savePos--;
        }
        i--;
    }
    return min(rightAnswer, leftAnswer);
}

int main()
{
    int n;
    char str[500005];
    char saveStr[500005];
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

    cin >> n;  
    cin >> str;
    
    strcpy(saveStr, str);
    int answerR = move(str, 'R');
    int answerB = move(saveStr, 'B');
    cout << min(answerR, answerB);
}