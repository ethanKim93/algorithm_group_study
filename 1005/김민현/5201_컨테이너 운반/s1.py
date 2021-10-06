import sys
sys.stdin = open('sample_input.txt')


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split()) #N: 컨테이너수 M: 트럭 수
    wi = list(map(int,input().split())) #wi 화물의 무게
    ti = list(map(int, input().split()))#트럭의 적재 용량
    ans = 0
    wi.sort(reverse=True)
    for idxN,i in enumerate(wi):
        min_weight = i
        min_idx = -1
        for idxM,j in enumerate(ti):
            a = 1
            if i<=j and min_weight >= (i - j):
                min_weight = (i - j)
                min_idx = idxM

        if min_idx != -1:
           ans += wi[idxN]
           ti.pop(min_idx)

    print('#{} {}'.format(tc,ans))