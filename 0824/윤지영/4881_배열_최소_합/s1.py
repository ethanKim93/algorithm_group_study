import sys
sys.stdin = open("sample_input.txt")

def board_sum(s,e):
    global N
    result = boards[s][e]
    answer = []
    for _ in range(N):
        exp_i = [s]
        exp_j = [e]
        for i in range(N):
            for j in range(N):
                if (i in exp_i) or (j in exp_j):
                    continue
                else:
                    result += boards[i][j]
                    exp_i.append(i)
                    exp_j.append(j)
        answer.append(result)
    r = answer[0]
    for k in range(len(answer)):
        if r > answer[k]:
            r = answer[k]
    return r


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    boards = [list(map(int, input().split())) for _ in range(N)]
    ans = board_sum(0,0)
    for i in range(N):
        for j in range(N):
            if ans > board_sum(i,j):
                ans = board_sum(i,j)
    print(ans)


