import sys

input = sys.stdin.readline

string1 = input().strip()
string2 = input().strip()

len_string1 = len(string1)
len_string2 = len(string2)

array = [0] * len_string2

for i in range(len_string1):
    cnt = 0
    for j in range(len_string2):
        if (cnt < array[j]):
            cnt = array[j]
        elif (string2[j] == string1[i]):
            array[j] = cnt + 1

print(max(array))
