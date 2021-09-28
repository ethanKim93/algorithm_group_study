import sys

sys.stdin = open('input.txt')
T = int(input())


def in_order(n):
    global visit
    if n:
        in_order(left[n])
        visit.append(n)
        in_order(right[n])

for tc in range(1, T + 1):
    V = int(input())
    left = [0] * (V + 1)
    right = [0] * (V + 1)


    for i in range(V):
        if 2 * i <= V:
            left[i] = 2 * i
        if 2 * i + 1 <= V:
            right[i] = 2 * i + 1
    visit = [0]

    in_order(1)

    root = 0
    findv = 0
    print(visit)
    # 루트와 N//2번 노드의 값 구하기
    for i in range(len(visit)):
        if visit[i] == 1:
            root = i
        if visit[i] == (V // 2):
            findv = i
    print('#{} {} {} '.format(tc, root, findv))
