import sys
sys.stdin = open('input.txt')
from pprint import pprint

def prim(li):
    li[0] = 0
    visited[0] = 1
    for i in range(1, N):
        li[0] = ((x_list[0]-x_list[i])**2) + ((y_list[0] - y_list[i])**2)
    for i in range(N):
        u = 0
        min_cost = INF
        for j in range(N):
            if min_cost > li[j] and not visited[j]:
                u = j
                min_cost = li[j]
        visited[u] = 1
        for k in range(1, N):
            if not visited[k]:
                newone = ((x_list[u]-x_list[k])**2) + ((y_list[u] - y_list[k])**2)
                if li[k] > newone:
                    li[k] = newone
    return sum(li)*E

for tc in range(1, int(input())+1):
    ans = 0
    INF = 987654321
    N = int(input())                                # 섬 수
    x_list = list(map(int, input().split()))        # x좌표
    y_list = list(map(int, input().split()))        # y좌표
    E = float(input())                              # 세금 / E*(길이**2)
    mat = [INF]*N
    visited = [0]*N
    ans = round(prim(mat))

    print('#{} {}'.format(tc, ans))