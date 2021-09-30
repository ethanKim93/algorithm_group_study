import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    flag = 'ON'                                 # flag 기본값 'ON'
    for i in range(N):                          # N회 순회돌면서
        if M & (1 << i) == 0:                   # 2^0 ~ 2^(N-1)까지의 비트 중에 0이 있는 경우
            flag = 'OFF'                        # flag 의 값을 'OFF'로 변경하고 순회 종료
            break

    print('#{} {}'.format(tc, flag))