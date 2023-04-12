import sys

array = sys.stdin.readline().split("-")
sub_sum = []

for element in array:
    sub_arr = list(map(int, element.split("+")))
    sub_sum.append(sum(sub_arr))
    
result = sub_sum[0]
for i in range(1, len(sub_sum)):
    result -= sub_sum[i]
print(result)