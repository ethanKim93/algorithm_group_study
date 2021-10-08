import sys
sys.stdin = open('input.txt')

def work(idx, person):
    global result

    if idx <= result:
        return

    if person == N:
        if result <= idx:
            result = idx
        return

    for i in range(N):
        if not visited[i]:
            # 방문한 다음에 idx값 보고 다시 돌아오기
            visited[i] = 1
            work(idx * arr[person][i] * 0.01, person + 1)
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    # 최대값 구하는거니까 0으로 설정
    result = 0
    work(1, 0)
    print('#{} {:.6f}'.format(tc, result*100))