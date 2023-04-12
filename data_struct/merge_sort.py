from heapq import merge
from typing import Sequence, MutableSequence

def merge_sorted_list(a: Sequence, b: Sequence, c: MutableSequence)-> None:
    pa, pb, pc = 0, 0, 0
    na, nb, nc = len(a), len(b), len(c)
    while pa < na and pb < nb:
        if a[pa] < b[pb]:
            c[pc] = a[pa]
            pc += 1
            pa += 1
        else:
            c[pc] = b[pb]
            pc += 1
            pb += 1
        
    while pa < na:
        c[pc] = a[pa]
        pc += 1
        pa += 1
    while pb < nb:
        c[pc] = b[pb]
        pc += 1
        pb += 1

def merge_sort(arr, left, right):
	if right == left:
		return
	elif right - left == 1:
		if arr[right] < arr[left]:
			arr[right], arr[left] = arr[left], arr[right]
		return
	
	center = (left + right) // 2
	left_arr = arr[left:center]
	right_arr = arr[center:right + 1]
	merge_sort(left_arr, 0, len(left_arr) - 1)
	merge_sort(right_arr, 0, len(right_arr) - 1)
	merge_sorted_list(left_arr, right_arr, arr)

if __name__ == '__main__':
	arr = [324,246,75,836,587,79,87345,246,1,-245, -134526, -74654, 0, 24554]
	merge_sort(arr, 0, len(arr) - 1)
	print(arr)
