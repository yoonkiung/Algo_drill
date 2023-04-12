def shaker(arr):
    left = 0
    right = len(arr) - 1
    last = right

    while left < right:
        for j in range(left, right):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                last = j
        right = last

        for j in range(right, left, -1):
            if arr[j - 1] > arr[j]:
                arr[j - 1],  arr[j] = arr[j], arr[j - 1]
                last = j
        left = last
    return arr

if __name__ == '__main__':
    arr = [1342,2435,2456,57,638,624,3136,1]
    shaker(arr)
    print(arr)