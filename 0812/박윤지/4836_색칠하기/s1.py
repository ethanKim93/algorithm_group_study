import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    for s in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        if color == 1:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if [i, j] not in red:
                        red.append([i, j])
        if color == 2:
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    if [i, j] not in blue:
                        blue.append([i, j])
    purple = 0
    for dot in red:
        if dot in blue:
            purple += 1
    print('#{} {}'.format(tc, purple))