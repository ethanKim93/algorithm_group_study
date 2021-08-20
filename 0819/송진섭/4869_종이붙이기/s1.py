import sys
sys.stdin = open('sample_input.txt')


def paper(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return (paper(n-2)*2) + paper(n-1)



T= int(input())
for tc in range(1, T+1):
    N = int(input())
    answer = paper(N//10)
    print('#{} {}'.format(tc, answer))
