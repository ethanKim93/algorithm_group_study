# 풀려서 어이없네

import sys
sys.stdin = open('sample_input.txt')

def nCr(n, r, s, k):
    global ans
    if k == r:
        # print(comb)
        comb2 = [m for m in range(0, N)]    # comb가 A음식, comb2가 B음식
                                            # 식재료 모두 포함한 리스트 만들고
        for l in range(0, r):
            if comb[l] in comb2:
                comb2.remove(comb[l])       # A음식에 들어간 식재료는 제거함
        # print(comb2)
        total = 0                           # A음식 시너지 합
        total2 = 0                          # B음식 시너지 합
        for j in range(0, r):               # [0, 1, 2, 3, 4] 면 하나씩 선택하고
            for k in range(j+1, r):         # 선택한 식재료의 오른쪽 요소들로 2개씩 짝을 지음
                total += ingre[comb[j]][comb[k]] + ingre[comb[k]][comb[j]]
                total2 += ingre[comb2[j]][comb2[k]] + ingre[comb2[k]][comb2[j]]
        minus = abs(total - total2)         # abs()로 A,B의 시너지 차를 구함
        if minus < ans:
            ans = minus                     # 이번 조합으로 구한 차가 ans보다 작으면 ans에 저장
    else:
        for i in range(s, n-r+k+1):
            comb[k] = i
            nCr(n, r, i+1, k+1)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ingre = [list(map(int, input().split())) for _ in range(N)]
    ans = 987654321
    comb = [0] * (N//2)                     # A음식 식재료 조합
    nCr(N, N//2, 0, 0)
    print('#{} {}'.format(tc, ans))