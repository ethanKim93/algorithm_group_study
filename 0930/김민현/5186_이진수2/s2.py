import sys
sys.stdin = open('input.txt')

# 최종코드 (안재현)
T = int(input())
for tc in range(T):
    N = float(input())
    result = ''
    #while len(result) < 13:
    while True:
        N *= 2
        arr = str(N).split('.')
        if arr[0] == '1':
            result += '1'
        else:
            result += '0'
        N = float('0.'+arr[1])

        if arr[1] == '0': break

        if len(result) == 13:
            result = 'overflow'
            break
    print('#{} {}'.format(tc + 1, result))