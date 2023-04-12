def solution(board, skill):
    answer = 0

    n = len(board)
    m = len(board[0])
    new = []
    for i in range(n + 2):
        temp = [0] * (m + 2)
        new.append(temp)
    for sk in skill:
        type = sk[0]
        r1 = sk[1]
        c1 = sk[2]
        r2 = sk[3]
        c2 = sk[4]
        degree = sk[5]
        if type == 1:
            degree = -degree
        new[r1+1][c1+1] += degree
        new[r2+2][c1+1] -= degree
        new[r1+1][c2+2] -= degree
        new[r2+2][c2+2] += degree

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            new[i][j] = new[i][j] + new[i - 1][j] + new[i][j - 1] - new[i - 1][j - 1]

    for i in range(n):
        for j in range(m):
            if board[i][j] + new[i + 1][j + 1] > 0:
                answer += 1
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])