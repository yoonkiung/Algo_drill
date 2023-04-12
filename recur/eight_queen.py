pos = [0] * 8
flag_low = [False] * 8
flag_right_diagonal = [False] * 15
flag_left_diagonal = [False] * 15

def put() -> None:

    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int) -> None:

    for j in range(8):
        if  (not flag_low[j]
            and not flag_right_diagonal[i + j]
            and not flag_left_diagonal[i - j + 7]):
            
            pos[i] = j
            if i == 7:
                put()
            else:
                flag_low[j] = True
                flag_right_diagonal[i + j] = True
                flag_left_diagonal[i - j + 7] = True
                set(i + 1)
                flag_low[j] = False
                flag_right_diagonal[i + j] = False
                flag_left_diagonal[i - j + 7] = False

set(0)

