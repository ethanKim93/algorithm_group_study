import sys
sys.stdin = open('sample_input.txt')


def bfs(N, M, count):
    print(N)
    if N == M:
        print('a')
        return
    else:
        count += 1
        if 0 < N + 1 <= 1000000 and N != M:
            print("{}횟수".format(N))
            bfs(N + 1, M, count)
            print('1번')
        if 0 < N - 1 <= 1000000 and N != M:
            bfs(N - 1, M, count)
            print('2번')
        if 0 < N * 2 <= 1000000 and N != M:
            bfs(N * 2, M, count)
            print('3번')
        if 0 < N - 10 <= 1000000 and N != M:
            bfs(N - 10, M, count)
            print('4번')
    return


for t in range(int(input())):
    N, M = map(int, input().split())
    count = 0
    print('#{} {}'.format(t + 1, bfs(N, M, 0)))