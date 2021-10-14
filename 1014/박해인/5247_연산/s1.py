import sys
sys.stdin = open('sample_input.txt')

def calculate(N):
    count = [0] * 1000001
    queue, front = [N], 0
    count[N] = 0

    while True:
        N = queue[front]
        for c in [1, -1, N, -10]:
            if N + c == M:
                return count[N]+1
            if 0 <= N+c < 1000001 and not count[N+c]:
                count[N+c] = count[N]+1
                queue.append(N+c)
        front += 1


T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(test_case, calculate(N)))
