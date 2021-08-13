import sys
sys.stdin = open('sample_input.txt')

A = int(input())
for tc in range(0, A):

    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    empty = [[0] * 10 for _ in range(10)]
    cnt = 0

    for i in range((len(arr))):
        for k in range(arr[i][0], arr[i][2]+1):
            for l in range(arr[i][1], arr[i][3]+1):
                if arr[i][4] == 1:
                    if empty[k][l] == 1:
                        empty[k][l] = 1
                    elif empty[k][l] != 1:
                        empty[k][l] += 1
                elif arr[i][4] == 2:
                    if empty[k][l] == 2:
                        empty[k][l] = 2
                    elif empty[k][l] != 2:
                        empty[k][l] += 2
    for a in range(len(empty)):
        for s in range(len(empty[a])):
            if empty[a][s] > 2:
                cnt += 1
    print('#{} {}'.format(tc+1, cnt))
