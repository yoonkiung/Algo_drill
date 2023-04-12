import sys

if __name__ == '__main__':
	n = int(sys.stdin.readline())

	arr = []
	for i in range(n):
		arr.append(int(sys.stdin.readline()))
	arr.sort()
	print(*arr, sep='\n')