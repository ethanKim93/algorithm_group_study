import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1,t+1):
    V,E = map(int,input().split())
    border = [[] for _ in range(V+1)]
    for _ in range(E):
        start, end = map(int,input().split())
        border[start].append(end)
    S,G = map(int,input().split())

    visit = [0] * (V+1)

    # DFS가 온전히 이해가 어려워서 초기 셋팅값만 이해했습니다. 부족한 개념 채워넣겠습니다 ㅠ