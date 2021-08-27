import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N은 화덕의 크기, M은 피자 개수
    C = list(map(int, input().split()))
    # C는 M개의 피자에 뿌려진 치즈의 양

    P = []
    for index, cheese in enumerate(C):
        P.append([index + 1, cheese])

    queue = []
    for i in range(N):
        queue.append(P.pop(0))

    bin = []
    while len(queue) > 1:
        if len(queue) < N and P:
            queue.append(P.pop(0))

        pzcz = queue.pop(0)
        if pzcz[1] // 2 == 0:
            bin.append(pzcz)
        else:
            pzcz[1] //= 2
            queue.append(pzcz)

    print('#{} {}'.format(tc, queue[0][0]))
