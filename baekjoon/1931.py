import sys

n = int(sys.stdin.readline())

array = []

for i in range(n):
    sub_array = list(map(int, sys.stdin.readline().split()))
    array.append(sub_array)

array.sort(key = lambda x: x[0])
array.sort(key = lambda x: x[1])

print(array)

# count = 0
# end_time = 0
# for element in array:
#     if (end_time <= element[0]):
#         count += 1
#         end_time = element[1]

# print(count)