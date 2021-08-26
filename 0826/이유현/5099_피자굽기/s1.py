import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    queue = []
    for i in range(M):
        queue.append([i+1, pizza[i]])

    oven = []
    for _ in range(N):
        oven.append(queue.pop(0))

    while len(oven) > 1:
        # 공간이 비었는데 피자가 아직 남아있다면 추가해준다.
        if len(oven) < N and queue:
            oven.append(queue.pop(0))
        check = oven.pop(0)
        num, cheese = check[0], check[1]

        if cheese // 2 == 0:
            continue
        else:
            oven.append([num, cheese // 2])
    print('#{} {}'.format(tc, oven.pop(0)[0]))
