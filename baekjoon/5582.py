str1 = input().strip()
str2 = input().strip()

table = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

max_value = 0
for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if (str1[i - 1] == str2[j - 1]):
            table[i][j] = table[i - 1][j - 1] + 1
            max_value = max(table[i][j], max_value)
print(max_value)
