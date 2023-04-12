def qsort(arr, left, right):
    pl = left
    pr = right
    mid = arr[(left + right) // 2]

    while pl <= pr:
        while arr[pl] < mid:
            pl += 1
        while arr[pr] > mid:
            pr -= 1
        if pl <= pr:
            arr[pl], arr[pr] = arr[pr], arr[pl]
            pl += 1
            pr -= 1
    if left < pr:
        qsort(arr, left, pr)
    if right > pl:
        qsort(arr, pl, right)
    

if __name__ == '__main__':
    arr = [3,425,46,58,69,74,63,25,234,13,1,346,47,58,69,-1, -1, 3, 46]
    qsort(arr, 0, len(arr) - 1)
    print(arr)