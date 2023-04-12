import sys
input = sys.stdin.readline

str1 = input().strip()
str2 = input().strip()

d = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if (str1[i - 1] == str2[j - 1]):
            d[i][j] = d[i - 1][j - 1] + 1
        else:
            d[i][j] = max(d[i - 1][j], d[i][j - 1])

max_value = max(d[len(str1)])
# for ele in d:
#     print(ele)
if (max_value == 0):
    print(0)
    exit()

i = len(str1)
j = len(str2)
sub_array = []

while (max_value > 0):
    if (d[i][j] == d[i - 1][j]):
        i -= 1
    elif (d[i][j] == d[i][j - 1]):
        j -= 1
    else:
        sub_array.append(str2[j - 1])
        i -= 1
        j -= 1
        max_value -= 1

sub_array.reverse()
print(len(sub_array))
for ele in sub_array:
    print(ele, end="")