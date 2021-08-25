import sys
sys.stdin = open('sample_input.txt')

def check(idx, subsum):
    global minsum
    if subsum > minsum:         # 종료조건. 재귀중인 함수의 현재 합이 최소 합보다 크면 종료
        return
    if idx == len(table[0]):    # idx가 끝까지 돌았을 때 종료
        if subsum < minsum:     # 만약 최소 합을 찾았다면 최신화
            minsum = subsum
        return

    for k in range(len(table[0])):
        if visited[k] == 0:                       # k 열에 방문하지 않았을 경우
            visited[k] = 1                        # 방문 기록
            check(idx+1, subsum+table[idx][k])    # 함수 호출시에 인자에 합을 직접 더해서 전달한다.
            visited[k] = 0                        # 방문기록 초기화

for tc in range(1, int(input())+1):
    N = int(input())
    minsum = 10*N       # 최소값 비교를 위한 변수, 나올수 있는 최대값으로 초기화
    visited = [0] * N   # 방문 여부를 기록할 배열
    table = [list(map(int,input().split())) for _ in range(N)]
    check(0, 0)
    print('#{} {}'.format(tc, minsum))
