import sys
sys.stdin = open('input.txt')


def check(idx):
    global start, minist
    # 2 : 구하고자 하는건 최소값인데, 예를 들어 1~2열에서 이미 이전에 구한 최소값보다 크다면
    # 3열을 확인할 필요가 없다! 따라서 이러한 경우의 수를 줄이기 위해 , 메모이제이션
    if start >= minist:
        return
    # 3 : 3열까지 다 구했을 때, 최소값 찾기
    if idx == N:
        if start < minist:
            minist = start
            return
    else:
        for i in range(N):
            if visited[i] == 0:
                # 4 : 하나의 열에서 방문안한 데이터를 더해주고 그 다음 열로 넘겨주기
                visited[i] = 1
                start += arr[idx][i]
                check(idx+1)
                # 5 : 넘겨주고 나서는 다른 경우의 수를 따져야 하기 때문에,
                # 방문했다는 것과 계산 추가해준 것을 원상태로 돌려놓기
                visited[i] = 0
                start -= arr[idx][i]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    # 1 : 모든 경우의 수를 다 따져볼 예정이라, 조건에 맞는 결과를 얻기 위해 전역변수 만들어놓기
    start = 0
    minist = 1000000000

    check(0)

    print('#{} {}'.format(tc, minist))