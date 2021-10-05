"""
1번에서 출발해서 -> N-1개 (N-1!) -> 다시 1번으로
0번부터 출발해서 -> 1 ~ N-1(N-1개) -> 다시 0번으로 (인덱스 관리)
"""
import sys
sys.stdin = open('sample_input.txt')


# 순열
def perm(k, cost):                  # cost: 배터리 사용량
    global ans
    if cost >= ans: return          # 가지치기 - cost가 현재 ans보다 크거나 같음(최소비용 x)
    if k == N:
        cost += G[order[N-1]][0]    # 마지막에 방문한 번호(N-1)에서 [0]으로 가는 번호 누적
        ans = min(ans, cost)        # 최솟값 갱신
    else:
        for i in range(k, N):
            order[k], order[i] = order[i], order[k]    # 순서 바꾸고
            # 이때 누적 사용량은 "현재 사용량(cost) + 이전 사용량"
            perm(k+1, cost + G[order[k-1]][order[k]])  # 다음 확인
            order[k], order[i] = order[i], order[k]    # 원상 복구


T = int(input())
for tc in range(1, T+1):
    # 구역의 개수
    N = int(input())
    # 인접 행렬
    G = [list(map(int, input().split())) for _ in range(N)]
    # 방문 순서 배열
    order = [i for i in range(N)]
    ans = N*100

    perm(1, 0)                      # 배터리 사용량 0부터 시작
    print('#{} {}'.format(tc, ans))