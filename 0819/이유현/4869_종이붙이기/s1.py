import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def paper(n):
    if n == 2:
        return 3
    elif n == 1:
        return 1
    return paper(n-1) + paper(n-2)*2

for tc in range(1, T+1):
    N = int(input()) // 10
    cnt = paper(N)
    print('#{} {}'.format(tc, cnt))



