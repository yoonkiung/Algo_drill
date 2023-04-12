def bubble_sort(arr):
    n = len(arr)
    compare = 0
    
    for i in range(n - 1):
        change = 0
        for j in range(0, n - i - 1):
            compare += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                change += 1
        if change == 0: #이미 정렬된 경우에 최적화
            break
    print(f'compare = {compare}')
    # print(arr)
    return arr

if __name__ == '__main__':
    arr = [1342,2435,2456,57,638,624,3136,1]
    bubble_sort(arr)
    print(arr)