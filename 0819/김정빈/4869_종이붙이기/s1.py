import sys
sys.stdin = open("input.txt")

def paper(N):
    if N == 1:
        return 1
    elif N == 2:
        return 3
    else:
        return paper(N-2)*2 + paper(N-1)

T = int(input())
for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, paper(N)))

    #규칙: 홀수일때 *2+1 짝수일때 *2-1