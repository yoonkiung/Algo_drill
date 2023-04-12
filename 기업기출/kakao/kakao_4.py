answer = [None] * 11
max = 0

def cal_score(ryan, apc):
    score = 0
    for i in range (11):
        if ryan[i] > apc[i]:
            score += 10 - i
        elif ryan[i] == 0 and apc[i] == 0:
            continue
        else:
            score -= 10 - i
    return score

def recur(ryan, apc, arrow, index):
    global max
    if index == 11:
        ryan[10] += arrow
        cur_score =  cal_score(ryan, apc)
        print(f'cur_score : {cur_score}')
        if cur_score >= max:
            max = cur_score
            for i in range(11):
                answer[i] = ryan[i]
        ryan[10] -= arrow
        return
    
    if apc[index] < arrow:
        ryan[index] +=  apc[index] + 1
        recur(ryan, apc, arrow - apc[index] - 1, index + 1)
        ryan[index] -=  apc[index] + 1

    recur(ryan, apc, arrow, index + 1)

def solution(n, info):
    ryan = [0] * 11
    recur(ryan, info, n, 0)
    if max == 0:
        return [-1]
    return answer

print(solution(5, [2,1,1,1,0,0,0,0,0,0,0]))