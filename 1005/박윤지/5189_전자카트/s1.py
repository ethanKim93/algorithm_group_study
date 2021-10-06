import sys
sys.stdin = open('sample_input.txt', 'r')

# 문제에서는 사무실이 1,1 이지만, -1씩 해서 0,0으로 바꿔서 풀었다

# 순열 생성 함수
def perm(n, k):
    if k == n:
        global ans
        if ans > calc(P):  # 배터리 소비량 계산 함수
            ans = calc(P)
        return
    else:
        for j in range(k, n):
            P[k], P[j] = P[j], P[k]
            perm(n, k+1)
            P[k], P[j] = P[j], P[k]
            

def calc(arr):
    sumN = batt[0][P[0]]
    for m in range(0, N-2):
        sumN += batt[arr[m]][arr[m+1]]
    # sumN += batt[P[0]][P[1]]
    # sumN += batt[P[1]][P[2]]
    # sumN += batt[P[2]][P[3]]
    sumN += batt[P[N-2]][0]
    return sumN


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    batt = [list(map(int, input().split())) for _ in range(N)]
    ans = 999999999999
    # 1, 2, 3, ... N-1 수들의 순열 구하기
    P = [i for i in range(1, N)]
    perm(len(P), 0)
    print('#{} {}'.format(tc, ans))