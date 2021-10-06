import sys
sys.stdin = open('sample_input.txt')

dr = [1, 0]
dc = [0, 1]  # 하 우

def get_minimum(r, c, tmp_sum):
    global min_sum

    if min_sum < tmp_sum:  # 최소값이 아니면 return
        return

    if (r, c) == (N-1, N-1):
        if tmp_sum < min_sum:
            min_sum = tmp_sum  # 최소값 갱신
        return

    for d in range(2):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N:  # 유효성 검사
            get_minimum(nr, nc, tmp_sum+data[nr][nc])

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10 * N  # 최대값으로 초기화
    get_minimum(0, 0, data[0][0])

    print('#{} {}'.format(test_case, min_sum))

