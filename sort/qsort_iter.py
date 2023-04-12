from stack_deque import Stack

def qsort_iter(arr, left, right):
    stack = Stack(right - left + 1)

    stack.push((left, right))

    while not stack.is_empty():
        pl, pr = left, right = stack.pop()
        mid = arr[(pr + pl) // 2]

        while arr[pl] < mid:
            pl += 1
        while arr[pr] > mid:
            pr -= 1
        
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1

        if left < pr:
            stack.push((left, pr))
        if pl < right:
            stack.push((pl, right))        

if __name__ == '__main__':
    arr = [3,425,46,58,69,74,63,25,234,13,1,346,47,58,69,-1, -1, 3, 46]
    qsort_iter(arr, 0, len(arr) - 1)
    print(arr)
