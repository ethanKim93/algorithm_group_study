import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    result = ''
    cnt = 0
    while True:
        next_num = N * 2
        result += str(int(next_num))
        N = next_num - int(next_num)
        cnt += 1
        if N == 0.0:
            print('#{} {}'.format(tc, result))
            break
        if cnt > 13:
            print('#{} overflow'.format(tc))
            break
