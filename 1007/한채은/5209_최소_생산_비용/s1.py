import sys
sys.stdin = open('sample_input.txt')

# 비용계산하는 함수
# 돌아야하는 열의 위치와 누적 합 값 가지고 있음
def cost(idx, total):
    global result
    # 가지치기
    # 완전 탐색을 막기 위해 가지고 있는 합계가 result보다 크면
    # 더 돌아봤자 소용 없으니까 그냥 return
    if total >= result:
        return

    # 열값이 N과 같으면 끝까지 다 돈거니까 return
    if idx == N:
        if total < result:
            result = total
        return

    # i는 행을 의미함
    for i in range(N):
        # 방문 안했으면
        if not visited[i]:
            # 방문표시 한 다음에 다음 인덱스값 보고 다시 돌아오기
            visited[i] = 1
            cost(idx+1, total + arr[idx][i])
            # 방문 0으로 초기화
            visited[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 방문배열
    visited = [0] * N
    # 임의의 큰 수 (최소비용)
    result = 9999999
    # cost함수 시작
    cost(0, 0)

    print('#{} {}'.format(tc, result))