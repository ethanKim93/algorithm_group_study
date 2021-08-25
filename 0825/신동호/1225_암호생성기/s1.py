import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    pws = list(map(int, input().split()))
    i = 1
    while pws[0] - i > 0:
        pws.append(pws.pop(0)-i)
        i = i % 5 + 1
    else:
        pws.pop(0)
        pws.append(0)
    print('#{}'.format(N), end = ' ')
    print(' '.join(map(str, pws)))