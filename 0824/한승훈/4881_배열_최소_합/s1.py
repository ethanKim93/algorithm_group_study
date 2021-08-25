import sys
sys.stdin = open('sample_input.txt')


def min_sum(start):
    global min_ans, ans
    # 제한시간 초과가 나오므로 가지치기를 진행
    if ans > min_ans:
        return

    if start == N:  # 덧셈 완료
        if ans < min_ans:
            min_ans = ans
        return

    for j in range(N):
        if visited[j] == 0:  # 방문한곳인지 확인
            visited[j] = 1
            ans += matrix[start][j]
            min_sum(start+1)
            # 위에 min_sum(start+1)이 j를 방문했을때 기준으로 계산하므로 초기화 필요
            visited[j] = 0
            ans -= matrix[start][j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for _ in range(N)]
    ans = 0
    min_ans = 90  # 최대 숫자 9 * 최대 N값 10
    min_sum(0)
    print('#{} {}'.format(tc, min_ans))




