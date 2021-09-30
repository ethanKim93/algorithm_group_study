import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = input()

    ans = ''
    cnt = 0
    n = 0
    while True:
        num_2 = int(float(N)*2)
        N = float(N)*2 - num_2
        ans += str(num_2)
        cnt += 1
        n += 1
        if cnt >= 13 or N == 0:
            break
    if cnt >= 13:
        print('#{} overflow'.format(tc))
    else:
        print('#{} {}'.format(tc, ans))
