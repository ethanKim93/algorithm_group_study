import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    knm_list = list(map(int, input().split()))
    K = knm_list[0]
    N = knm_list[1]
    M = knm_list[2]
    bs_list = list(map(int, input().split()))

    for idx in range(0, M-1):
        if bs_list[idx+1] - bs_list[idx] > K:
            print('#{} {}'.format(tc, 0))
            break
    else:
        location = 0
        bs_cnt = 0
        while location < N - K:
            for id in range(M - 1, -1, -1):
                if bs_list[id] <= location + K:
                    location = bs_list[id]
                    bs_cnt += 1
                    break
        print('#{} {}'.format(tc, bs_cnt))






