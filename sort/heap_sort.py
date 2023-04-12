def heap_sort(arr):

    def down_heap(arr, left, right):
        parent = left
        temp = arr[left]

        while parent < (right + 1) // 2:
            cl = parent * 2 + 1
            cr = cl + 1
            child = cr if cr <= right and arr[cr] > arr[cl]  else cl
            if temp > arr[child]:
                break
            arr[parent] = arr[child]
            parent = child
        arr[parent] = temp
    
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        down_heap(arr, i, n - 1)
    
    for i in range(n - 1):
        arr[0], arr[n - 1 - i] = arr[n - 1 - i], arr[0]
        down_heap(arr, 0, n - 2 - i)
    
                
arr = [5, 6,7, 6, 43,1, 1435, 2564,563,4678,4562,342,2457,234,61345,2465,3576,3568,4769,479]
heap_sort(arr)
print(arr)