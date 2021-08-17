import sys

sys.stdin = open('input.txt')


def HoriStr(Listring,M,N):
    for i in range(M):
        strfind = ''
        for k in range(M-N+1): #1
            for j in range(k,k+N):
                strfind += Listring[i][j]
            print(strfind)
            strdefind = ''
            for m in range(len(strfind) - 1, -1, -1):
                strdefind += strfind[m]
            result = ''
            if strdefind == strfind:
                result += strdefind
                return result
            else:

                continue




def VertiStr(Listring,M,N):

    for i in range(M): #0~19
        strfind = ''
        for k in range(0,M-N+1): #8 0~7
            for j in range(k,k+N): #0~13, 1~14, ...7~20
                    strfind += Listring[j][i]

            strdefind = ''
            for m in range(len(strfind) - 1, -1, -1):
                strdefind += strfind[m]

            result = ''
            if strdefind == strfind:
                result += strdefind
                return result
            else:
                continue





T = int(input())
for tc in range(1, T + 1):

    M, N = map(int, input().split())
    Listring = [list(map(str, sys.stdin.readline().split('\n')[0])) for _ in range(N)]

    result1 = VertiStr(Listring,M,N)
    result2 = HoriStr(Listring,M,N)

    print(result1,result2)

    # print('#{} {}'.format(tc, result))
