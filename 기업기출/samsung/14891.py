import sys
from collections import deque

input = sys.stdin.readline

def rotate_right(que: deque) -> None:
    que.rotate(1)

def rotate_left(que: deque) -> None:
    que.rotate(-1)

def is_same(first: deque, second: deque) -> bool:
    if (first[2] == second[6]):
        return (True)
    return (False)

one = deque(list(map(int, input().strip())))
two = deque(list(map(int, input().strip())))
three = deque(list(map(int, input().strip())))
four = deque(list(map(int, input().strip())))

k = int(input().strip())
rots = []
for i in range(k):
    rots.append(list(map(int, input().strip().split())))

for rot in rots:
    if (rot[0] == 1):
        if (rot[1] == 1):
            flag = is_same(one, two)
            rotate_right(one)
            if (not flag):
                flag = is_same(two, three)
                rotate_left(two)
                if (not flag):
                    flag = is_same(three, four)
                    rotate_right(three)
                    if (not flag):
                        rotate_left(four)
        else:
            flag = is_same(one, two)
            rotate_left(one)
            if (not flag):
                flag = is_same(two, three)
                rotate_right(two)
                if (not flag):
                    flag = is_same(three, four)
                    rotate_left(three)
                    if (not flag):
                        rotate_right(four)
    elif (rot[0] == 2):
        if (rot[1] == 1):
            flag_left = is_same(one, two)
            flag_right = is_same(two, three)
            rotate_right(two)
            if (not flag_left):
                flag = is_same(two, three)
                rotate_left(one)
            if (not flag_right):
                flag = is_same(three, four)
                rotate_left(three)
                if (not flag):
                    rotate_right(four)
        else:
            flag_left = is_same(one, two)
            flag_right = is_same(two, three)
            rotate_left(two)
            if (not flag_left):
                flag = is_same(two, three)
                rotate_right(one)
            if (not flag_right):
                flag = is_same(three, four)
                rotate_right(three)
                if (not flag):
                    rotate_left(four)
    elif (rot[0] == 3):
        if (rot[1] == 1):
            flag_left = is_same(two, three)
            flag_right = is_same(three, four)
            rotate_right(three)
            if (not flag_left):
                flag = is_same(one, two)
                rotate_left(two)
                if (not flag):
                    rotate_right(one)
            if (not flag_right):
                rotate_left(four)
        else:
            flag_left = is_same(two, three)
            flag_right = is_same(three, four)
            rotate_left(three)
            if (not flag_left):
                flag = is_same(one, two)
                rotate_right(two)
                if (not flag):
                    rotate_left(one)
            if (not flag_right):
                rotate_right(four)
    else:
        if (rot[1] == 1):
            flag = is_same(three, four)
            rotate_right(four)
            if (not flag):
                flag = is_same(two, three)
                rotate_left(three)
                if (not flag):
                    flag = is_same(one, two)
                    rotate_right(two)
                    if (not flag):
                        rotate_left(one)
        else:
            flag = is_same(three, four)
            rotate_left(four)
            if (not flag):
                flag = is_same(two, three)
                rotate_right(three)
                if (not flag):
                    flag = is_same(one, two)
                    rotate_left(two)
                    if (not flag):
                        rotate_right(one)
    # print(one)
    # print(two)
    # print(three)
    # print(four)
    # print()
point = one[0] + \
        (two[0] * 2) + \
        (three[0] * 4) + \
        (four[0] * 8)

print(point)
