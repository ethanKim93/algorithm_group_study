import sys
sys.stdin=open('input.txt')

T= int(input())
# 첫 줄에 컨테이너 수 N과 트럭 수 M이 주어지고,
# 다음 줄에 N개의 화물이 무게wi,
# 다음 줄에 M개 트럭의 적재용량 ti가 주어진다.
for tc in range(1,T+1):
    N,M=map(int,input().split())
    wi=list(map(int, input().split()))
    ti=list(map(int, input().split()))
    answer = 0
    while ti and wi:
        truck = ti.pop()
        while wi:
            container = wi.pop()
            if truck >= container:
                answer += container
            break


    print('#{} {}'.format(tc, answer))
