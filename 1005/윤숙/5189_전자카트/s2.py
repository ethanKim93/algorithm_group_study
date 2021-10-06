#진석님 코드
import sys
sys.stdin = open('input.txt')

def search(start):
    global total, min_total

    if min_total < total:                       # 현재까지의 경로 합이 최소 합보다 크다면 종료
        return

    if sum(visited) == N-1:                     # 사무실 돌아오기 직전까지 N-1번의 지점에 방문했다면 종료
        if total+table[start][0] < min_total:   # 최소값 갱신
            min_total = total
            min_total += table[start][0]        # 사무실로 돌아오는길 추가
        return

    for i in range(1, N):
        if not visited[i] and i != start:       # 방문한 적이 없고, 현재 구역과 같은 번호가 아닐 때
            visited[i] = 1                      # 방문 표시
            total += table[start][i]            # 경로 합 추가
            search(i)                           # 다음 경로 이동
            visited[i] = 0                      # 방문 표시 해제
            total -= table[start][i]            # 합 갱신

for tc in range(1, int(input())+1):
    N = int(input())            # 총 관리구역
    table = [list(map(int,input().split())) for _ in range(N)]  # 배터리 소비량
    visited = [0] * N           # 방문여부( 0 ~ (N-1) )
    total = 0                   # 경로의 합
    min_total = N*100           # 최소 합(최댓값으로 초기화)
    search(0)                   # 탐색 시작
    print('#{} {}'.format(tc, min_total))