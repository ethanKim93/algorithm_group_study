import sys
sys.stdin = open('input.txt')


def Bbit_print(i):
    output = ''
    for j in range(N-1, -1, -1):                      # N자리
        output += '1' if i & (1 << j) else '0'      # i의 j자리 비트가 1인지 확인
    return output


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    res = Bbit_print(M)
    ans = 'ON'
    for i in res:
        if i == '0':
            ans = 'OFF'
            break
    print('#{} {}'.format(tc, ans))

