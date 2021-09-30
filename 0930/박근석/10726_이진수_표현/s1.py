import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    for i in range(N):
        if (1 << i) & M:
            pass
        else:
            print('#{} {}'.format(tc, 'OFF'))
            break
    else:
        print('#{} {}'.format(tc, 'ON'))

    # for i in bin(M)[2:][len(bin(M)[2:])-N:]:
    #     if i == '0':
    #         print('#{} {}'.format(tc, 'OFF'))
    #         break
    # else:
    #     print('#{} {}'.format(tc, 'ON'))


    # if '0' in bin(M)[2:][len(bin(M)[2:])-N:]:
    #     print('#{} {}'.format(tc, 'OFF'))
    # else:
    #     print('#{} {}'.format(tc, 'ON'))
