import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):

    M, N = map(int, input().split())
    Listring = [list(map(str, input().split())) for _ in range(N)]

    for i in range(0, len(Listring)):
        strfind = ''
        for j in range(0, len(Listring[0])):
            strfind += Listring[i][j]

        strdefind = ''
        for k in range(len(strfind) - 1, -1, -1):
            strdefind += strfind[k]

        if strdefind == strfind:
            break
        else: continue

    print('#{} {}'.format(tc, strdefind))
