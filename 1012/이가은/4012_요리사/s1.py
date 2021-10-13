import sys
sys.stdin = open('sample_input.txt')

def delicious(li):
    flavor=0
    for i in range(N//2):
        for j in range(i+1,N//2):
            flavor += recipe[li[i]][li[j]]+recipe[li[j]][li[i]]
    return flavor

def combi(n, k):
    global result
    if n == N//2:
        A = []
        B = []
        for i in range(N):
            if visited[i]:
                A.append(i)
            else:
                B.append(i)

        flavor_A = delicious(A)
        flavor_B = delicious(B)

        if abs(flavor_A-flavor_B) < result:
            result = abs(flavor_A-flavor_B)
        return

    for j in range(k, N):
        if not visited[j]:
            visited[j] = 1
            combi(n+1, k+1)
            visited[j] = 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    recipe = [list(map(int, input().split())) for _ in range(N)]
    visited = [0 for i in range(N)]
    answer_list = []
    result = 987654321

    combi(0,0)
    print('#{} {}'.format(tc, result))