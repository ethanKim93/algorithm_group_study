import sys
sys.stdin = open('input.txt')

# 최종 (장지빈)
def check(point, s, cnt):   # check(시작point, 현재까지 비용 합, 남은 이동횟수)
    global ans
    if cnt == 1:            # 남은 이동횟수가 1이라면 무조건 사무실로 돌아가야 한다.
        if s + matrix[point][0] < ans: # 현재까지 비용 합 + 사무실 이동비용과 ans 비교
            ans = s + matrix[point][0]  # 작다면 ans에 넣어주고 리턴
        return
    if s >= ans:  # 이때까지 저장한 비용이 현재 최저비용보다 높다면 바로 리턴(가지치기)
        return
    for i in range(1, N):  # 사무실은 마지막에 방문하기 위해 1부터 N-1번까지 이동
        if not visited[i]:  # 방문하지 않은 골프장이라면
            visited[i] = 1  # 방문체크를 해주고
            check(i, s + matrix[point][i], cnt-1)  # 현위치에 i, 현재까지 비용 + 이동할 비용, 남은 이동횟수 -1
            visited[i] = 0 # 다음 함수에서 이동할 수도 있으므로 visited 초기화

for tc in range(1, int(input())+1):
    N = int(input())        # 이동 가능 횟수
    matrix = [list(map(int, input().split())) for _ in range(N)]   # 배열
    ans = 0   # 정답을 담을 변수
    for i in range(N):   # 배열 내 최대 비용값(*배열 전체 합)
        ans += sum(matrix[i])
    visited = [1] + [0]*N    # 방문표시 (첫 시작 사무실은 마지막에 돌아오기 위해 [1]+[0]*N)
    check(0, matrix[0][0], N)   # check(시작point, 현재까지 비용 합, 남은 이동횟수)

    print('#{} {}'.format(tc, ans))