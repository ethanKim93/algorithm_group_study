import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    node = [0] + list(map(int, input().split()))

    for i in range(2, N+1):
        while True:  # 크기에 따라 노드값 배열 변경
            if node[i//2] > node[i]:
                node[i//2], node[i] = node[i], node[i//2]
                i = i//2
            else:
                break
    total = 0
    n = N
    # 조상노드 합
    while n != 1:
        total += node[n // 2]
        n = n//2

    print(f'#{tc} {total}')
