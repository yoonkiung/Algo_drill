import sys

input = sys.stdin.readline

t = int(input().strip())

def swap(plane, x1, y1, x2, y2):
    temp = plane[x1][y1]
    plane[x1][y1] = plane[x2][y2]
    plane[x2][y2] = temp

def rotate_itself(plane, dir):
    if (dir == '-'):
        swap(plane, 0, 0, 0, 2)
        swap(plane, 0, 2, 2, 2)
        swap(plane, 2, 2, 2, 0)

        swap(plane, 0, 1, 1, 2)
        swap(plane, 1, 2, 2, 1)
        swap(plane, 2, 1, 1, 0)

    else:
        swap(plane, 0, 0, 2, 0)
        swap(plane, 2, 0, 2, 2)
        swap(plane, 2, 2, 0, 2)

        swap(plane, 0, 1, 1, 0)
        swap(plane, 1, 0, 2, 1)
        swap(plane, 2, 1, 1, 2)

def swap_multi(p1, x1, y1, p2, x2, y2):
    temp = p1[x1][y1]
    p1[x1][y1] = p2[x2][y2]
    p2[x2][y2] = temp

def rotate_front(top, bottom, front, back, left, right, dir):
    rotate_itself(front, dir)
    if (dir == '-'):
        swap_multi(top, 2, 0, right, 0, 0)
        swap_multi(right, 0, 0, bottom, 2, 2)
        swap_multi(bottom, 2, 2, left, 2, 2)

        swap_multi(top, 2, 2, right, 2, 0)    
        swap_multi(right, 2, 0, bottom, 2, 0)
        swap_multi(bottom, 2, 0, left, 0, 2)

        swap_multi(top, 2, 1, right, 1, 0)
        swap_multi(right, 1, 0, bottom, 2, 1)
        swap_multi(bottom, 2, 1, left, 1, 2)

    else:
        swap_multi(top, 2, 0, left, 2, 2)
        swap_multi(left, 2, 2, bottom, 2, 2)
        swap_multi(bottom, 2, 2, right, 0, 0)

        swap_multi(top, 2, 2, left, 0, 2)
        swap_multi(left, 0, 2, bottom, 2, 0)
        swap_multi(bottom, 2, 0, right, 2, 0)

        swap_multi(top, 2, 1, left, 1, 2)
        swap_multi(left, 1, 2, bottom, 2, 1)
        swap_multi(bottom, 2, 1, right, 1, 0)

def rotate_top(top, bottom, front, back, left, right, dir):
    rotate_itself(top, dir)
    
    if (dir == '-'):
        swap_multi(front, 0, 0, left, 0, 0)
        swap_multi(left, 0, 0, back, 0, 2)
        swap_multi(back, 0, 2, right, 0, 0)

        swap_multi(front, 0, 2, left, 0, 2)
        swap_multi(left, 0, 2, back, 0, 0)
        swap_multi(back, 0, 0, right, 0, 2)

        swap_multi(front, 0, 1, left, 0, 1)
        swap_multi(left, 0, 1, back, 0, 1)
        swap_multi(back, 0, 1, right, 0, 1)

    else:
        swap_multi(front, 0, 0, right, 0, 0)
        swap_multi(right, 0, 0, back, 0, 2)
        swap_multi(back, 0, 2, left, 0, 0)

        swap_multi(front, 0, 2, right, 0, 2)
        swap_multi(right, 0, 2, back, 0, 0)
        swap_multi(back, 0, 0, left, 0, 2)

        swap_multi(front, 0, 1, right, 0, 1)
        swap_multi(right, 0, 1, back, 0, 1)
        swap_multi(back, 0, 1, left, 0, 1)

def rotate_back(top, bottom, front, back, left, right, dir):
    
    if (dir == '-'):
        rotate_itself(back, '+')

        swap_multi(top, 0, 0, left, 2, 0)
        swap_multi(left, 2, 0, bottom, 0, 2)
        swap_multi(bottom, 0, 2, right, 0, 2)

        swap_multi(top, 0, 2, left, 0, 0)
        swap_multi(left, 0, 0, bottom, 0, 0)
        swap_multi(bottom, 0, 0, right, 2, 2)

        swap_multi(top, 0, 1, left, 1, 0)
        swap_multi(left, 1, 0, bottom, 0, 1)
        swap_multi(bottom, 0, 1, right, 1, 2)

    else:
        rotate_itself(back, '-')

        swap_multi(top, 0, 0, right, 0, 2)
        swap_multi(right, 0, 2, bottom, 0, 2)
        swap_multi(bottom, 0, 2, left, 2, 0)

        swap_multi(top, 0, 2, right, 2, 2)
        swap_multi(right, 2, 2, bottom, 0, 0)
        swap_multi(bottom, 0, 0, left, 0, 0)

        swap_multi(top, 0, 1, right, 1, 2)
        swap_multi(right, 1, 2, bottom, 0, 1)
        swap_multi(bottom, 0, 1, left, 1, 0)

def rotate_bottom(top, bottom, front, back, left, right, dir):

    if (dir == '-'):
        rotate_itself(bottom, '+')

        swap_multi(front, 2, 0, right, 2, 0)
        swap_multi(right, 2, 0, back, 2, 2)
        swap_multi(back, 2, 2, left, 2, 0)

        swap_multi(front, 2, 2, right, 2, 2)
        swap_multi(right, 2, 2, back, 2, 0)
        swap_multi(back, 2, 0, left, 2, 2)

        swap_multi(front, 2, 1, right, 2, 1)
        swap_multi(right, 2, 1, back, 2, 1)
        swap_multi(back, 2, 1, left, 2, 1)

    else:
        rotate_itself(bottom, '-')

        swap_multi(front, 2, 0, left, 2, 0)
        swap_multi(left, 2, 0, back, 2, 2)
        swap_multi(back, 2, 2, right, 2, 0)

        swap_multi(front, 2, 2, left, 2, 2)
        swap_multi(left, 2, 2, back, 2, 0)
        swap_multi(back, 2, 0, right, 2, 2)

        swap_multi(front, 2, 1, left, 2, 1)
        swap_multi(left, 2, 1, back, 2, 1)
        swap_multi(back, 2, 1, right, 2, 1)

def rotate_right(top, bottom, front, back, left, right, dir):
    rotate_itself(right, dir)

    if (dir == '-'):
        swap_multi(front, 0, 2, top, 0, 2)
        swap_multi(top, 0, 2, back, 2, 2)
        swap_multi(back, 2, 2, bottom, 2, 2)

        swap_multi(front, 2, 2, top, 2, 2)
        swap_multi(top, 2, 2, back, 0, 2)
        swap_multi(back, 0, 2, bottom, 0, 2)

        swap_multi(front, 1, 2, top, 1, 2)
        swap_multi(top, 1, 2, back, 1, 2)
        swap_multi(back, 1, 2, bottom, 1, 2)

    else:
        swap_multi(front, 0, 2, bottom, 2, 2)
        swap_multi(bottom, 2, 2, back, 2, 2)
        swap_multi(back, 2, 2, top, 0, 2)

        swap_multi(front, 2, 2, bottom, 0, 2)
        swap_multi(bottom, 0, 2, back, 0, 2)
        swap_multi(back, 0, 2, top, 2, 2)

        swap_multi(front, 1, 2, bottom, 1, 2)
        swap_multi(bottom, 1, 2, back, 1, 2)
        swap_multi(back, 1, 2, top, 1, 2)

def rotate_left(top, bottom, front, back, left, right, dir):
    rotate_itself(left, dir)

    if (dir == '-'):
        swap_multi(top, 0, 0, front, 0, 0)
        swap_multi(front, 0, 0, bottom, 2, 0)
        swap_multi(bottom, 2, 0, back, 2, 0)

        swap_multi(top, 2, 0, front, 2, 0)
        swap_multi(front, 2, 0, bottom, 0, 0)
        swap_multi(bottom, 0, 0, back, 0, 0)

        swap_multi(top, 1, 0, front, 1, 0)
        swap_multi(front, 1, 0, bottom, 1, 0)
        swap_multi(bottom, 1, 0, back, 1, 0)

    else:
        swap_multi(top, 0, 0, back, 2, 0)
        swap_multi(back, 2, 0, bottom, 2, 0)
        swap_multi(bottom, 2, 0, front, 2, 0)

        swap_multi(top, 2, 0, back, 0, 0)
        swap_multi(back, 0, 0, bottom, 0, 0)
        swap_multi(bottom, 0, 0, front, 2, 0)

        swap_multi(top, 1, 0, back, 1, 0)
        swap_multi(back, 1, 0, bottom, 1, 0)
        swap_multi(bottom, 1, 0, front, 1, 0)

for i in range(t):
    n = int(input().strip())
    infos = input().strip().split()

    top = [['w' for _ in range(3)] for _ in range(3)]
    bottom = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]

    for info in infos:
        if (info[0] == 'U'):
            rotate_top(top, bottom, front, back, left, right, info[1])
        elif (info[0] == 'D'):
            rotate_bottom(top, bottom, front, back, left, right, info[1])
        elif (info[0] == 'F'):
            rotate_front(top, bottom, front, back, left, right, info[1])
        elif (info[0] == 'B'):
            rotate_back(top, bottom, front, back, left, right, info[1])
        elif (info[0] == 'L'):
            rotate_left(top, bottom, front, back, left, right, info[1])
        elif (info[0] == 'R'):
            rotate_right(top, bottom, front, back, left, right, info[1])
    
        # for ele in top:
        #     print(ele)
        # print()

    for i in range(3):
        for j in range(3):
            print(top[i][j], end = "")
        print()