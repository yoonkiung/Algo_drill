import sys

if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())
    orig = list(map(int, sys.stdin.readline().split()))
    arr = [0 for i in range(n + 1)]
    for i in range(m):
        order = list(map(int, sys.stdin.readline().split()))
        start = order[0] - 1
        last = order[1] - 1
        degree = order[2]
       
        arr[start] += degree
        arr[last + 1] -= degree
    new = []
    for i in range(1, n + 1):
        arr[i] += arr[i - 1]
        new.append(arr[i - 1] + orig[i - 1])
    print(*new, sep=' ')