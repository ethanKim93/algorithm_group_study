import sys

sys.stdin = open('input.txt')


def HoriStr(Listring):
    for i in range(len(Listring)):
        strfind = ''
        for j in range(len(Listring[i])):
            strfind += Listring[i][j]

        strdefind = ''
        for k in range(len(strfind) - 1, -1, -1):
            strdefind += strfind[k]
        result = ''
        if strdefind == strfind:
            result += strdefind
            return result
        else:
            strdefind = ''
            continue

    return -1


def VertiStr(Listring):

    for i in range(0,len(Listring[0])):
        strfind = ''
        for j in range(0,len(Listring)):
            strfind += Listring[j][i]
        strdefind = ''
        for k in range(len(strfind) - 1, -1, -1):
            strdefind += strfind[k]
            result = ''
        if strdefind == strfind:
            result += strdefind
            return result
        else:
            continue

    return -1



T = int(input())
for tc in range(1, T + 1):

    M, N = map(int, input().split())
    Listring = [list(map(str, sys.stdin.readline().split('\n')[0])) for _ in range(N)]
    print(Listring)
    result1 = VertiStr(Listring)
    result2 = HoriStr(Listring)
    print(result1,result2)
    # print('#{} {}'.format(tc, result))
