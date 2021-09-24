import sys
sys.stdin = open('sample_input.txt')

def search(cnt):
    global cnt
    while cnt > 1:
        node[cnt // 2] += node[cnt]
        cnt -= 1


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for i in range(M):
        cnt, val = map(int, input().split())
        node[cnt] = val

    search(N)
    print("#{} {}".format(tc + 1, node[L]))