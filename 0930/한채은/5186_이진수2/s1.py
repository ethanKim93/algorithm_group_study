import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())

    ans = ''
    # 2의 -1승부터 2의 -12승까지 돌면서 나눈 몫을 ans에 담아주기
    for i in range(-1, -13, -1):
        ans += str(int(N//2**i))
        # 나머지 N
        N = N % (2**i)
        # N이 0이면 이진수로 변환
        if N == 0:
            break
    # 아니면 overflow
    else:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))
