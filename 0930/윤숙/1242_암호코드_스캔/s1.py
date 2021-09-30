# 16진수의 길이 2진수 길이
# 1개 =길이 14  14 *4 =56
# 2개 =길이 28  28 *4 =112
# 3개 =길이 42  42 *4 =168
# 4개 =길이 56  56 *4 =224
# 5개 =길이 70  70 *4 =280

import sys
sys.stdin=open('input.txt')


hexfind=set()
T=int(input())
for tc in range(1,8):
    #세로N 가로M

    N,M=map(int,input().split())
    #암호코드 찾기
    # 1. 뒤에서 부터 찾는다.
    # 2. 위의 행이 0인경우에 읽는다. -> 0이 아닌경우 pass하고 지나간다.
    pattern=set()

    for i in range(N):
        n = ''
        tmp=input()
        for j in range(M):
            n+=tmp[j]
        pattern.add(n)
    print(pattern)
    for i in range(len(pattern))
