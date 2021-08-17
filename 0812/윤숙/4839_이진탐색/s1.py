import sys

sys.stdin = open('sample_input.txt')
T = int(input())
def binerySearch(find):
    ST = 1
    EN = totalN
    Cnt = 1
    while ST <= EN:

        Mid = (ST + EN) // 2
        if find == Mid:
            Cnt += 1
            break
        elif find > Mid:
            ST = Mid
            Cnt += 1
        elif find < Mid:
            EN = Mid
            Cnt += 1

    return Cnt

for tc in range(1, T + 1):
    totalN, findA, findB = map(int, input().split())


    R1=binerySearch(findA)
    R2=binerySearch(findB)

    result=''
    if R1<R2:
        result='A'
    elif R1>R2:
        result='B'
    elif R1==R2:
        result='0'

    print('#{} {}'.format(tc,result))