#최종코드-이주현
T = int(input())

def max_val(N):
    result = 0
    for i in range(N):
        for j in range(N):
            result += matrix[i][j]
    return result

def search(now, summary):
    global result

    if len(visited) == len(matrix):                 # 모든 구역을 돌았으면
        summary += matrix[now][0]                   # 다시 사무실로 돌아가는 값 더하고 return
        if result > summary:
            result = summary
        return

    for nxt in range(len(matrix)):                  # 관리구역 만큼 반복
        if nxt not in visited and nxt != now:       # 방문하지 않은 구역 & 현위치가 아닐 때
            summary += matrix[now][nxt]             # nxt (방문할 구역) 방문 -> 배터리 소모
            visited.append(nxt)
            search(nxt, summary)                    # 재귀 현위치(now) -> nxt

            visited.pop()                           # 재귀 종료시 모든 방문한 관리구역 pop
            summary -= matrix[now][nxt]             # 배터리 소모량 초기화

                                                    # 다음 관리구역부터 for문 시작


for tc in range(1, 1+ T):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = max_val(N)                             # 초기 result 값으로 큰 값 지정

    visited = [0, ]
    search(0, 0)    # 맨 처음 위치(사무실)
    print("#{} {}".format(tc, result))