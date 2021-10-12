import sys
sys.stdin = open('input.txt')

def work(result, person):  # result: 확률 계산해가는 값 , person:깊이,i번째사람
    global max_result
    global visited

    if result <= max_result: # 시간초과 방지를 위한 백트래킹
        return
    # base case
    if person == N:  # 모든 직원이 각 자 일을 맡아 다 할때, 최종결과랑 비교
        if max_result <= result:
            max_result = result
        return
    # recursion case
    for j in range(N):  # 전체를 도는데
        if visited[j] == 0:  # 방문을 안했으면
            visited[j] = 1  # 방문한다
            work(result * arr[person][j] * 0.01, person + 1)  # 재귀 DFS
            visited[j] = 0  # 방문다했다


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 인원수, 일 능률
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_result = 0  # 비교할 최대 확률
    work(1, 0)


    print('#{} {:.6f}'.format(tc, max_result * 100))