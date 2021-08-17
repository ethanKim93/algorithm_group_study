import sys
sys.stdin = open('input.txt')


def HoriStr(Listring,M,N):

    for i in range(M):

        for k in range(M-N+1):
            strfind = ''
            for j in range(k,k+N):
                if i < N and j < M:
                    strfind += Listring[i][j]

            strdefind = ''
            for m in range(len(strfind) - 1, -1, -1):
                strdefind += strfind[m]
            result = ''
            if strdefind == strfind:
                result += strdefind
                return result
            else:
                strfind = ''
                strdefind = ''
                continue


def VertiStr(Listring,M,N):

    for i in range(M): #0~19
        for k in range(0,M-N+1):
            strfind = ''
            for j in range(k,k+N):
                    if j<N and i<M:
                        strfind += Listring[j][i]

            strdefind = ''
            for m in range(len(strfind) - 1, -1, -1):
                strdefind += strfind[m]

            result = ''
            if strdefind == strfind:
                result += strdefind
                return result
            else:
                strfind = ''
                strdefind = ''
                continue





T = int(input())
for tc in range(1, T + 1):

    M, N = map(int, input().split())
    Listring = [list(map(str, sys.stdin.readline().split('\n')[0])) for _ in range(N)]

    result1 = VertiStr(Listring,M,N)
    result2 = HoriStr(Listring,M,N)

    if result1:
        print('#{} {}'.format(tc, result1))
    elif result2:
        print('#{} {}'.format(tc, result2))



