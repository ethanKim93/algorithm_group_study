import sys
sys.stdin = open('sample_input.txt')


def caces(n):
    global c
    if 2 <= n//10 and len(c) <= n//10:
        if (n // 10) % 2:
            c.append(caces(n-10) * 2 - 1)
        else:
            c.append(caces(n-10) * 2 + 1)
    return c[n//10]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    c = [0, 1]
    print('#{} {}'.format(tc, caces(N)))
