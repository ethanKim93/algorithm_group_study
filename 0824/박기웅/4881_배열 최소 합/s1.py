import sys
sys.stdin = open("sample_input.txt")


def arr_sum(idx, subsum):
    global min_sum
    # 부분합 진행 중 min_sum 보다 크면 더 돌 필요가 없음
    if subsum > min_sum:
        return
    # 다 돈 경우 subsum과 비교하여 min_sum 갱신
    if idx == N:
        if subsum < min_sum:
            min_sum = subsum
        return
    # col[j]가 0, 즉 방문안한 경우 재귀를 통해 부분합 갱신
    for j in range(N):
        if not col[j]:
            col[j] = 1
            arr_sum(idx+1, subsum + arr[idx][j])
            col[j] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    col = [0]*N
    min_sum = 9*N   # 최대 9*N 
    arr_sum(0, 0)
    print('#{} {}'.format(tc, min_sum))


