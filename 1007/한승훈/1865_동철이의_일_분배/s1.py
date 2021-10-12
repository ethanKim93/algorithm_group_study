import sys
sys.stdin = open('input.txt')

def cal(idx, prob):
    global max_prob
    if max_prob >= prob:  # 가지치기 (=기호를 안넣으면 시간초과가 뜸 주의!)
        return
    if idx > N-1:
        max_prob = max(max_prob, prob)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            cal(idx+1, prob * probablity[idx][i]/100)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    probablity = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_prob = 0
    cal(0,1)
    print('#{} {:.6f}'.format(tc, max_prob*100))
