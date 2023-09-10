import sys
import copy
input = sys.stdin.readline

r, c, m = list(map(int, input().split()))

info_shark = [{} for _ in range(c)]
for i in range(m):
    x, y, s, d, z = list(map(int, input().split()))
    info_shark[y - 1][x - 1] = [x - 1, y - 1, s, d, z]

for i in range(c):
    if (len(info_shark[i]) > 0):
        info_shark[i] = dict(sorted(info_shark[i].items()))
def find_dir(d, s):
    if (d == 1):
        return ([-s, 0])
    elif (d == 2):
        return ([s, 0])
    elif (d == 3):
        return ([0, s])
    else:
        return ([0, -s])

def move_shark():
    global info_shark
    c_info_shark = [{} for _ in range(c)]
    for col in range(c):
        if (len(info_shark[col]) == 0):
            continue
        for key in info_shark[col]:
            x, y, s, d, z = info_shark[col][key]
            nx = x
            ny = y
            if (d == 1 or d == 2):
                i = s % ((r - 1) * 2)
                while (i > 0):
                    if (d == 1):
                        if (nx - 1 < 0):
                            nx += 1
                            d = 2
                        else:
                            nx -= 1
                    else:
                        if (nx + 1 >= r):
                            nx -= 1
                            d = 1
                        else:
                            nx += 1
                    i -= 1
            else:
                i = s % ((c - 1) * 2)
                while (i > 0):
                    if (d == 3):
                        if (ny + 1 >= c):
                            ny -= 1
                            d = 4
                        else:
                            ny += 1
                    else:
                        if (ny - 1 < 0):
                            ny += 1
                            d = 3
                        else:
                            ny -= 1
                    i -= 1
            if (nx in c_info_shark[ny]):
                if (z > c_info_shark[ny][nx][4]):
                    c_info_shark[ny][nx] = [nx, ny, s, d, z]
            else:
                c_info_shark[ny][nx] = [nx, ny, s, d, z]
    info_shark = c_info_shark
        
count = 0
for j in range(c):
    if (len(info_shark[j]) > 0):
        if (len(info_shark[j]) > 1):
            info_shark[j] = dict(sorted(info_shark[j].items()))
        key = next(iter(info_shark[j]))
        count += info_shark[j][key][4]
        del info_shark[j][next(iter(info_shark[j]))]
    move_shark()
print(count)