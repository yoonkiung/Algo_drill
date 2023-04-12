import sys
import math
input = sys.stdin.readline

n, k= list(map(int, input().strip().split()))

print(math.comb(n, k) % 10007)

