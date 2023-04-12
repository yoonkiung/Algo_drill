
arr = []

def hanoi(no: int, x: int, y: int, count: int) -> int:
    z = -1
    if x + y == 3:
        z = 3
    elif x + y == 5:
        z = 1
    else:
        z = 2

    if (no <= 1):
        arr.append(f'{x} {y}')
        return (count + 1)
    elif (no == 2):
        arr.append(f'{x} {z}')
        arr.append(f'{x} {y}')
        arr.append(f'{z} {y}')
        return (count + 3)
    else:
        temp = hanoi(no - 1, x, z, count)
        arr.append(f'{x} {y}')
        temp = hanoi(no - 1, z, y, temp)
        return (temp + 1)

if __name__ == '__main__':
    print(hanoi(int(input()), 1, 3, 0))
    for string in arr:
        print(string)