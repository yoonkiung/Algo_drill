import sys

input = sys.stdin.readline

n = int(input().strip())
array = list(map(int, input().strip().split()))
rev_array = array[::-1]

dp_inc = [1 for _ in range(n)]
dp_dec = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if (array[j] < array[i]):
            dp_inc[i] = max(dp_inc[i], dp_inc[j] + 1)
        if (rev_array[j] < rev_array[i]):
            dp_dec[i] = max(dp_dec[i], dp_dec[j] + 1)

result = [0 for i in range(n)]
for i in range(n):
    result[i] = dp_inc[i] + dp_dec[n - i - 1] - 1    

print(max(result))
