import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    w = sorted(list(map(int,input().split())))[::-1]
    capa = sorted(list(map(int,input().split())))[::-1]
    weight = 0
    i = 0 # 전체 트럭을 넣어봄
    j = 0
    while i < M:
        if capa[i] >= w[j]: # 옮길 수 있으면 다음 화물
            weight += w[j]
            j += 1
        else:
            j += 1
            if j == N:
                break
            continue
        i += 1
        if j == N or i == M:
            break
    print('#{} {}'.format(tc,weight))