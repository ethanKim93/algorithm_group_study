import sys
sys.stdin = open('sample_input.txt')

def cal(i):
    global total, min_diff
    if i >= N:
        return
    if sum(visited) == num:
        lst1 = []
        lst2 = []
        tot1 = 0
        tot2 = 0
        for idx, val in enumerate(visited):
            if val:
                lst1.append(idx)
            else:
                lst2.append(idx)
        for u in range(num):
            for v in range(num):
                tot1 += recipe[lst1[u]][lst1[v]]
                tot2 += recipe[lst2[u]][lst2[v]]
        min_diff = min(min_diff, abs(tot1 - tot2))
        return
    visited[i] = 1
    cal(i+1)
    visited[i] = 0
    cal(i+1)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    recipe = [list(map(int, input().split())) for _ in range(N)]
    min_diff = 100000
    num = N//2
    visited = [0] * N
    cal(0)
    print('#{} {}'.format(tc,min_diff))