import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    NM = list(map(int, input().split()))
    N, M = NM[0], NM[1]

    v = list(map(int, input().split()))

    add = 0
    max_num = 0
    min_num = 0
    for i in range(M):
        min_num += v[i] #초기값 설정
    for idx in range(N-M+1): # 한칸씩 계산
        for j in range(idx, M+idx): # M만큼 더하기
            add += v[j]
        if add > max_num:
            max_num = add
        if add < min_num:
            min_num = add
        add = 0
    print('#{} {}'.format(tc, max_num-min_num))

