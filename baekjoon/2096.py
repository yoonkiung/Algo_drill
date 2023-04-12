import sys
import copy
input = sys.stdin.readline

n = int(input().strip())

d_max = [[0, 0, 0] for _ in range(2)]
d_min = [[0, 0, 0] for _ in range(2)]

for i in range(n):
    
    array = list(map(int, input().strip().split()))
    if (i == 0):
        d_max[0] = copy.deepcopy(array)
        d_min[0] = copy.deepcopy(array)
    else:
        d_max[1][0] = array[0] + max(d_max[0][0], d_max[0][1])
        d_max[1][1] = array[1] + max(d_max[0][0], d_max[0][1], d_max[0][2])
        d_max[1][2] = array[2] + max(d_max[0][1], d_max[0][2])
        d_max[0] = copy.deepcopy(d_max[1])
        
        d_min[1][0] = array[0] + min(d_min[0][0], d_min[0][1])
        d_min[1][1] = array[1] + min(d_min[0][0], d_min[0][1], d_min[0][2])
        d_min[1][2] = array[2] + min(d_min[0][1], d_min[0][2])
        d_min[0] = copy.deepcopy(d_min[1])

print(max(d_max[0]), end=" ")
print(min(d_min[0]))
    