import sys
sys.stdin = open('sample_input.txt')

def back(idx, cnt):
    global min_cnt
    if min_cnt < cnt:  # 가지치기
        return
    if idx >= N-1:
        min_cnt = min(min_cnt, cnt)
        return

    charge = stations[idx]
    for i in range(charge+idx, idx, -1):
        back(i, cnt+1)


T = int(input())
for tc in range(1, T+1):
    N, *stations = map(int, input().split())
    min_cnt = 100
    back(0, -1)
    print('#{} {}'.format(tc, min_cnt))



    # 오답 : 테스트 케이스가 10 8 7 6 5 4 3 2 1 1 주어진다면 8번을 돌기에 안된다.
    # cnt = loc = 0
    # while True:
    #     move = 0
    #     charge = max(stations[loc:loc + charge])
    #     for idx, val in enumerate(stations[loc:loc+charge]):
    #         if val == charge:
    #             move = idx
    #     loc = loc + move + 1
    #     cnt += 1
    #     if loc + charge >= N-1:
    #         break
    # print('#{} {}'.format(tc, cnt))
