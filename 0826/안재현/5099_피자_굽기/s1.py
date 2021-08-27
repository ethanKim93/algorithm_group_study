import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    seq = list(map(int, input().split()))
    pit = []
    pit_cnt = 0
    res = []
    res_cnt = 0
    while len(seq) > 0 or len(pit) > 1:
        if len(pit) != N and len(seq) != 0:
            tmp = seq.pop(0)
            pit.append(tmp)
            pit_cnt += 1
            res.append(pit_cnt)
        elif len(pit) > 0:
            tmp = pit.pop(0)
            if tmp//2 == 0:
                res_cnt = res.pop(0)
            else:
                pit.append(tmp//2)
                res_cnt = res.pop(0)
                res.append(res_cnt)
                res = res

    print('#{} {}'.format(tc + 1, res[0]))