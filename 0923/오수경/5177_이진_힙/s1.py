import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node_num = list(map(int, input().split()))
    node = [0]*(N+1)

    for i in range(N):
        node[i+1] = node_num[i]

        while True:
            if i+1 == 1:
                break
            elif node[(i+1)//2] > node[i+1]:
                node[(i+1)//2], node[i+1] = node[i+1], node[(i+1)//2]
                i = (i+1)//2-1
            else:
                break
    total = 0
    n = N
    while n != 1:
        total += node[n // 2]
        n = n//2

    print(f'#{tc} {total}')
