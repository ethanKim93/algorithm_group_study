import sys
sys.stdin = open('input.txt')

T = int(input())

def check(puzzle):
    result = 0
    for i in range(len(puzzle)):
        row = 0
        col = 0
        for j in range(len(puzzle)):
            if puzzle[i][j]:
                row += 1
            elif row == K:
                row = 0
                result += 1
            else:
                row = 0

            if puzzle[j][i]:
                col += 1
            elif col == K:
                col = 0
                result += 1
            else:
                col = 0

    return result

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    puzzle = [list(map(int, input().split()))+[0] for _ in range(N)] + [[0]*(N+1)]
    print('#{} {}'.format(tc,check(puzzle)))