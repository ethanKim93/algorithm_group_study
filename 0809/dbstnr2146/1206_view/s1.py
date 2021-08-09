'''
h[i]와 h[i-2]h[i-1] h[i+1] h[i+2]넷 중 가장 높은 높이와의 차이는 조망권이 된다.
i는 2이상 부터  n-3칸의 위치 까지 탐색

'''
import sys
sys.stdin=open('input.txt')
T=10
for tc in range(1,T+1):
    N=int(input())
    buildings=list(map(int,input().split()))

    count=0
    for i in range(2,N-2):

        MaxV= buildings[i-2]

        if MaxV<buildings[i-1]:
            MaxV=buildings[i-1]
        if MaxV<buildings[i+1]:
            MaxV = buildings[i + 1]
        if MaxV<buildings[i+2]:
            MaxV=buildings[i+2]
        if buildings[i]>MaxV:
            count += buildings[i] - MaxV
    print('#{} {}'.format(tc, count))








